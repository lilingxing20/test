#!/usr/bin/python
# #coding:utf-8
# from wsgiref.simple_server
#
from wsgiref.simple_server import make_server
import json

class Dispatcher(object):
    def _match(self,method):
        URL_PATTERNS= ( ('GET/','GET_METHOD'), ('PUT/','PUT_METHOD'), )
        method = method
        for url,app in URL_PATTERNS:
            if method in url:
                return app
    def __call__(self,environ, start_response):
        #path = environ.get('PATH_INFO','/')
        #env = [environ[i] for i in environ ]
        method = environ['REQUEST_METHOD'] #
        print environ
        app = self._match(method)
        if app :
            app = globals()[app]
            return app(environ, start_response)
        else:
            start_response("404 NOT FOUND",[('Content-type', 'text/plain')])
            return ["Page dose not exists!"]
def GET_METHOD(environ, start_response):
    print "=================== start ==================="
    print [(var, environ[var]) for var in environ ]
    print "==================== end ===================="
    print "you called get method"
    start_response("200 OK",[('Content-type', 'text/html')])
    return ["Get method %s exist" % (environ['PATH_INFO'][1:] or '/') ]

def PUT_METHOD(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    print("request_body_size is %d " %(request_body_size))
    request_body = environ['wsgi.input'].read(request_body_size)
    print request_body
    request_body = json.dumps(request_body)
    print request_body
    start_response("200 OK",[('Content-type', 'text/html')])
    return ["put method, the body size is %d" % (request_body_size)]


app = Dispatcher()
httpd = make_server('127.0.0.1', 8000, app)
print "Serving on port 8000..."
httpd.serve_forever()
