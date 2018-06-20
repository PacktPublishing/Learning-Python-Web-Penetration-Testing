#!/usr/bin/env
import requests
myheaders={'user-agent':'Iphone 6'}
r =  requests.post('http://httpbin.org/post',data={'name':'packt'})
print r.url
print 'Status code:'
print '\t[-]' + str(r.status_code) + '\n'

print 'Server headers'
print '****************************************'
for x in r.headers:
    print '\t' + x + ' : ' + r.headers[x]
print '****************************************\n'

print "Content:\n"
print r.text
