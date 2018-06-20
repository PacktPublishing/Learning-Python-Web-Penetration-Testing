import requests
from threading import Thread
import sys
import time
import getopt
import re
from termcolor import colored

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def banner():
    print "\n***************************************"
    print "* ForzaBruta Forms 0.5*"
    print "***************************************"


def usage():
    print "Usage:"
    print "		-w: url (http://somesite.com/FUZZ)"
    print "		-t: threads"
    print "		-f: dictionary file\n"
    print "example: forzabruta.py -w http://www.targetsite.com/FUZZ -t 5 -f common.txt\n"


class request_performer(Thread):
    def __init__(self, word, url, hidecode, payload):
        Thread.__init__(self)
        self.word = word.split("\n")[0]
        self.url = url.replace('FUZZ', self.word)
        if payload != "":
            self.payload = payload.replace('FUZZ', self.word)
        else:
		    self.payload=payload
        self.hidecode = hidecode

    def run(self):
        try:
            start = time.time()
            if self.payload == "":
                 r = requests.get(self.url)
                 elaptime = time.time()
                 totaltime = str(elaptime - start)[1:10]
            else:
                list=self.payload.replace("="," ").replace("&"," ").split(" ")
                payload = dict([(k, v) for k,v in zip (list[::2], list[1::2])])
                r = requests.post(self.url, data = payload)
                elaptime = time.time()
                totaltime = str(elaptime - start)[1:10]

            lines = str(r.content.count("\n"))
            chars = str(len(r._content))
            words = str(len(re.findall("\S+", r.content)))
            code = str(r.status_code)
	    if r.history != []:
                first = r.history[0]
                code = str(first.status_code)
            else:
                pass

            if self.hidecode != chars:
                if '200' <= code < '300':
                    print totaltime + "\t"  + colored(code,'green') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + r.headers["server"] + "\t" + self.word
                elif '400' <= code < '500':
                    print totaltime + "\t" + colored(code,'red') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines + "\t" + r.headers["server"] + "\t" +  self.word
                elif '300' <= code < '400':
                    print totaltime + "\t" + colored(code,'blue') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines + "\t"+ r.headers["server"] + "\t" + self.word
            else:
                pass
            i[0] = i[0] - 1  # Here we remove one thread from the counter
        except Exception, e:
            print e


def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "w:f:t:p:c:")
    except getopt.GetoptError:
        print "Error en arguments"
        sys.exit()
    hidecode = 000
    payload = ""
    for opt, arg in opts:
        if opt == '-w':
            url = arg
        elif opt == '-f':
            dict = arg
        elif opt == '-t':
            threads = arg
        elif opt == '-p':
            payload = arg
        elif opt == '-c':
            hidecode = arg
    try:
        f = open(dict, "r")
        words = f.readlines()
    except:
        print"Failed opening file: " + dict + "\n"
        sys.exit()
    launcher_thread(words, threads, url, hidecode, payload)


def launcher_thread(names, th, url, hidecode,payload):
    global i
    i = []
    resultlist = []
    i.append(0)
    print "-----------------------------------------------------------------------------------------------------------------------------------"
    print "Time" + "\t" + "\t code \t\tchars\t\twords\t\tlines"
    print "-----------------------------------------------------------------------------------------------------------------------------------"
    while len(names):
        try:
            if i[0] < th:
                n = names.pop(0)
                i[0] = i[0] + 1
                thread = request_performer(n, url, hidecode, payload)
                thread.start()

        except KeyboardInterrupt:
            print "ForzaBruta interrupted  by user. Finishing attack.."
            sys.exit()
        thread.join()
    return


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "ForzaBruta interrupted by user, killing all threads..!!"
