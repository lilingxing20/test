# --*-- coding: utf-8 --*--
# author: lixx
# email: lilingxing20@163.com
import eventlet
from eventlet.green import urllib2

urls = [
    "https://res3.lekan.com/video/13/47/57/E1/shot/5_314x224.jpg",
    "https://res3.lekan.com/video/13/47/57/E2/shot/5_314x224.jpg",
    "https://res3.lekan.com/video/13/47/57/E3/shot/5_314x224.jpg",
]

def fetch(url):
    return urllib2.urlopen(url).read()

pool = eventlet.GreenPool()

for body in pool.imap(fetch, urls):
    print("got body", len(body))

