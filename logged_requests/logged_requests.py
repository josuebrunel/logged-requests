from __future__ import absolute_import

import logging

from requests import Session

class LoggedRequests(Session):

    def __init__(self, *args, **kwargs):
        self.logger = kwargs.pop('logger', None)
        if not self.logger:
            from logged_requests.logger import DefaultLogger
            logging.setLoggerClass(DefaultLogger)
            self.logger = logging.getLogger('logged_requests')
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = False
        super(LoggedRequests, self).__init__(*args, **kwargs)

    def request(self, method, url, **kwargs):
        self.logger.info('%s %s' % (method, url),
            extra={'requests_url': url}
        )

        response = super(LoggedRequests, self).request(method, url, **kwargs)

        self.logger.debug('Request Headers: {}'.format(''.join([
            '%s: %s | ' % (k,v) for k,v in response.request.headers.items()
        ])))
        if response.request.body:
            self.logger.info('Request Payload: %r' %(response.request.body),
                extra={'requests_request_payload': '%r' %response.request.body})
        self.logger.info('Status code: %r' %(response.status_code),
            extra={'requests_response_status': response.status_code})
        resp_headers = ''.join([
            '%s: %s | ' % (k,v) for k,v in response.headers.items()
        ])
        self.logger.debug('Response Headers: %r' %resp_headers, extra={
            'requests_response_headers': resp_headers})
        content = response.content[:5000]
        self.logger.debug('Response Content: %r' % content,
            extra={'requests_response_content': content})

        return response
