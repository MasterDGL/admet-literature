"""Check public code URLs without changing curated publication records."""
import argparse
import csv
import json
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def classify(status):
    if 200 <= status < 400:
        return 'reachable'
    if status in (404, 410):
        return 'unavailable'
    if status in (401, 403, 429):
        return 'restricted_or_rate_limited'
    return 'retry_needed'


def check(url, timeout=15):
    result = {'url': url, 'final_url': url, 'http_status': '', 'status': '', 'detail': ''}
    for attempt in range(2):
        try:
            request = Request(url, headers={'User-Agent': 'ADMET-Literature-Link-Check/1.0'})
            with urlopen(request, timeout=timeout) as response:
                code = response.status
                result.update(final_url=response.url, http_status=code, status=classify(code), detail='')
        except HTTPError as error:
            result.update(final_url=error.url, http_status=error.code, status=classify(error.code), detail=str(error.reason))
        except (URLError, TimeoutError, OSError) as error:
            result.update(http_status='', status='retry_needed', detail=str(error))
        if result['status'] in ('reachable', 'restricted_or_rate_limited'):
            break
        if attempt == 0:
            time.sleep(1)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/code-links.csv')
    parser.add_argument('--fail-unavailable', action='store_true')
    args = parser.parse_args()
    papers = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))['papers']
    references = {}
    for paper in papers:
        if paper.get('code_url'):
            references.setdefault(paper['code_url'], []).append(paper['id'])
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(check, sorted(references)))
    for row in rows:
        row.update(paper_ids='; '.join(references[row['url']]), checked_at=now)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['paper_ids', 'url', 'final_url', 'http_status', 'status', 'detail', 'checked_at'])
        writer.writeheader()
        writer.writerows(rows)
    counts = Counter(row['status'] for row in rows)
    print(f'{len(rows)} unique URLs checked: {dict(counts)}')
    print(f'Report: {args.output}')
    if args.fail_unavailable and counts['unavailable']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
