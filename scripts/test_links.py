import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from check_links import check


class LinkCheckTests(unittest.TestCase):
    @patch('check_links.time.sleep')
    @patch('check_links.urlopen')
    def test_retries_unavailable_before_reporting(self, request, sleep):
        request.side_effect = HTTPError('https://example.org', 404, 'Not Found', {}, None)
        self.assertEqual(check('https://example.org')['status'], 'unavailable')
        self.assertEqual(request.call_count, 2)

    @patch('check_links.urlopen')
    def test_rate_limit_is_not_a_dead_link(self, request):
        request.side_effect = HTTPError('https://example.org', 429, 'Rate limited', {}, None)
        self.assertEqual(check('https://example.org')['status'], 'restricted_or_rate_limited')

    @patch('check_links.time.sleep')
    @patch('check_links.urlopen')
    def test_network_failure_does_not_claim_missing(self, request, sleep):
        request.side_effect = URLError('timed out')
        self.assertEqual(check('https://example.org')['status'], 'retry_needed')


if __name__ == '__main__':
    unittest.main()
