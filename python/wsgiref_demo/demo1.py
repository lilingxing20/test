# --*-- coding: utf-8 --*--
# author: lixx
# email: lilingxing20@163.com
# http://peak.telecommunity.com/wsgiref_docs/module-wsgiref.simpleserver.html
# http://www.jianshu.com/p/e7a958bc0f0f
from wsgiref.simple_server import make_server, demo_app

httpd = make_server('', 8000, demo_app)
print "Serving HTTP on port 8000..."

# Respond to requests until process is killed
httpd.serve_forever()

# Alternative: serve one request, then exit
##httpd.handle_request()
