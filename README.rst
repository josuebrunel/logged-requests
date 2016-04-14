Logged Requests
===============

|Build Status| |Documentation Status|

**logged_requests** is a simple wrapper around the *requests.Session* object. It captures *input and output* data of a *requests.Session* object.


Installation
============

.. code:: python

    pip install logged_requests

Quickstart
----------

.. code:: python

    >>> url = 'https://httpbin.org/post'
    >>> from logged_requests import LoggedRequests
    >>> req = LoggedRequests()
    >>> resp = req.post(url, json={"name":"jsoh"})
    2016-04-12 21:09:56 INFO logged_requests.logged_requests.request: POST https://httpbin.org/post
    2016-04-12 21:09:57 DEBUG logged_requests.logged_requests.request: Request Headers: Content-Length: 16    | Accept-Encoding: gzip, deflate | Accept: */* | User-Agent: python-requests/2.9.1 | Connection: keep-alive   | Content-Type: application/json |
    2016-04-12 21:09:57 INFO logged_requests.logged_requests.request: Request Payload: '{"name": "josh"}'
    2016-04-12 21:09:57 INFO logged_requests.logged_requests.request: Status code: 200
    2016-04-12 21:09:57 DEBUG logged_requests.logged_requests.request: Response Headers: 'Content-Length:   411 | Server: nginx | Connection: keep-alive | Access-Control-Allow-Credentials: true | Date: Tue, 12 Apr    2016 19:09:57 GMT | Access-Control-Allow-Origin: * | Content-Type: application/json | '
    2016-04-12 21:09:57 DEBUG logged_requests.logged_requests.request: Response Content: '{\n  "args": {},   \n  "data": "{\\"name\\": \\"josh\\"}", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept":   "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "16", \n    "Content-Type":   "application/json", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.9.1"\n  }, \n  "json": {\n    "name": "josh"\n  }, \n  "origin": "82.227.125.5", \n  "url":    "https://httpbin.org/post"\n}\n'

*LoggedRequests* object can be initiated with a custom logger. If not initiated with a logger, *logged_request* will initiate a default logger, with **StreamHandler** as default *handler* and **DEBUG** as default *loggging level*

.. code:: python

    >>> url = 'https://httpbin.org/post'
    >>> from logged_requests import LoggedRequests
    >>> req = LoggedRequests(my_custom_logger)

.. |Build Status| image:: https://travis-ci.org/josuebrunel/logged-requests.svg?branch=master
    :target: https://travis-ci.org/josuebrunel/logged-requests
.. |Documentation Status| image:: https://readthedocs.org/projects/logged-requests/badge/?version=latest
    :target: https://readthedocs.org/projects/logged-requests/?badge=latest
