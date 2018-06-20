import requests
url='http://httpbin.org/redirect-to'
payload = {'url':'http://www.bing.com'}
req = requests.get(url,params=payload)
print req.text
print "Response code: " + str(req.status_code)
for x in req.history:
        print str(x.status_code) + ' : ' + x.url
