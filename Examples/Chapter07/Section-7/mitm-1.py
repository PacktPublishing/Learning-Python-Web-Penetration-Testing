import sys

global history 
history = [] 

def request(context, flow):
	global history
	url = flow.request.url
	if url not in history:
		f = open('httplogs.txt', 'a+')
		f.write(flow.request.url + '\n')	
		f.close()
		history.append(url)
	else:
		pass
