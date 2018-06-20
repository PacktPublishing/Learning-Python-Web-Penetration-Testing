import sys

def request(context, flow):
	f = open('httplogs.txt', 'a+')
	f.write(flow.request.url + '\n')	
	f.close()
