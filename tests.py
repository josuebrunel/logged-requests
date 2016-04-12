import logging

import pytest

from httmock import urlmatch, HTTMock, response

from logged_requests import LoggedRequests

@pytest.fixture(params=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'FATAL'])
def log_level(request):
    return request.param

@urlmatch(netloc=r'(.*\.)?httpbin\.org$')
def httpbin_mock(url, request):
    return response(200, {"message":"Are you really josh ?"}, request=request)


def test_log_level(caplog, log_level):
    url = 'https://httpbin.org/post'

    logger = logging.getLogger('logged_requests')
    logger.setLevel(getattr(logging, log_level))

    with HTTMock(httpbin_mock):
        requests = LoggedRequests(logger=logger)
        response = requests.post(url, json={'name':'josh'})

    records = [ record for record in caplog.records() if record.name == 'logged_requests' ]

    records_length = len(records)

    if logger.level == 10:
        assert records_length == 6
    elif logger.level == 20:
        assert records_length == 3
    else:
        assert records_length == 0

    for record in records:
        if record.levelname in ('DEBUG','INFO'):
            if getattr(record, 'requests_url', None):
                assert record.requests_url == url

            if getattr(record, 'requests_request_payload', None):
                assert record.requests_request_payload == '\'{"name": "josh"}\''

            if getattr(record, 'requests_response_status', None):
                assert record.requests_response_status == response.status_code

        if record.levelname == 'DEBUG':
            if getattr(record, 'requests_response_headers', None):
                resp_headers = ''.join([
                    '%s: %s | ' % (k,v) for k,v in response.headers.items()
                ])
                assert resp_headers == record.requests_response_headers

            if getattr(record, 'requests_response_content', None):
                assert record.requests_response_content == response.content

