import requests
from threading import Thread
import sys
import time
import getopt
import re
from termcolor import colored



def banner():
    print "\n***************************************"
    print "* ForzaBruta 0.2*"
    print "***************************************"


def usage():
    print "Usage:"
    print "		-w: url (http://somesite.com/FUZZ)"
    print "		-t: threads"
    print "		-f: dictionary file"
    print "		-c: filter by status code"
    print "example: forzabruta.py -w http://www.targetsite.com/FUZZ -t 5 -f common.txt\n"


class request_performer(Thread):
    def __init__(self, word, url,hidecode):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('FUZZ', self.word)
            self.url = self.urly
            self.hidecode = hidecode
        except Exception, e:
            print e

    def run(self):
        try:
            r = requests.get(self.url)
            lines = str(r.content.count("\n"))
            chars = str(len(r._content))
            words = str(len(re.findall("\S+", r.content)))
            code = str(r.status_code)
            if self.hidecode != code:
                if '200' <= code < '300':
                    print  colored(code,'green') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t  "
                elif '400' <= code < '500':
                    print  colored(code,'red') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t  "
                elif '300' <= code < '400':
                    print  colored(code,'blue') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t  "
                else:
                    print  colored(code,'yellow') + "   \t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t  "

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
        opts, args = getopt.getopt(argv, "w:f:t:c:")
    except getopt.GetoptError:
        print "Error en arguments"
        sys.exit()
    hidecode = 000
    for opt, arg in opts:
        if opt == '-w':
            url = arg
        elif opt == '-f':
            dict = arg
        elif opt == '-t':
            threads = arg
        elif opt == '-c':
            hidecode = arg
    try:
        f = open(dict, "r")
        words = f.readlines()
    except:
        print"Failed opening file: " + dict + "\n"
        sys.exit()
    launcher_thread(words, threads, url,hidecode)


def launcher_thread(names, th, url,hidecode):
    global i
    i = []
    i.append(0)
    print "-------------------------------------------------------------------------------------------------------------"
    print "Code" + "\t\tchars\t\twords\t\tlines\t\tURL"
    print "-------------------------------------------------------------------------------------------------------------"
    while len(names):
        try:
            if i[0] < th:
                n = names.pop(0)
                i[0] = i[0] + 1
                thread = request_performer(n, url,hidecode)
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
