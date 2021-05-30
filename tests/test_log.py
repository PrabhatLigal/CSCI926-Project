import unittest
from unittest import mock
import random
from notebook import log


class TestLogRequest(unittest.TestCase):

    @mock.patch('notebook.log.prometheus_log_method')
    def test_log_request_json(self, mock_prometheus): #modified
        err_count = 0
        debug_count = 0
        warning_count = 0
        info_count = 0
        logger = mock.MagicMock()
        for code in random.choices([200, 500, 404], k=50):
            headers = {'Referer': 'test'}
            request = mock.Mock(
                request_time=mock.Mock(return_value=1),
                headers=headers,
                method='GET',
                remote_ip='1.1.1.1.',
                uri='/some/dumy/url'
            )
            handler = mock.MagicMock(
                request=request,
                get_status=mock.Mock(return_value=code)
            )
            if code < 300 or code == 304:
                debug_count += 1
            elif code < 400:
                info_count += 1
            elif code < 500:
                warning_count += 1
            else:
                err_count += 2
    
            log.log_request(handler, log=logger, log_json=True)
            # Since the status was 500 there should be two calls to log.error,
            # one with the request headers and another with the other request
            # parameters.
        self.assertEqual(err_count, logger.error.call_count)
        self.assertEqual(debug_count, logger.debug.call_count)
        self.assertEqual(warning_count, logger.warning.call_count)
        self.assertEqual(info_count, logger.info.call_count)
