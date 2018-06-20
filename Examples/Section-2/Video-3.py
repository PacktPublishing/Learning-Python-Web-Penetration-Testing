import requests
payload= {'url':'http://www.edge-security.com'}
r=requests.get('http://httpbin.org/redirect-to',params=payload)
print "Status code:"
print "\t *" + str(r.status_code)
