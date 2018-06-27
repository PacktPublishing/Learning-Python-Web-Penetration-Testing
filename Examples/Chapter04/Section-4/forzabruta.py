import requests
from threading import Thread
import sys
import getopt

def banner():
    print "\n***************************************"
    print "* ForzaBruta 0.1*"
    print "***************************************"

def usage():
    print "Usage:"
    print "		-w: url (http://somesite.com/FUZZ)"
    print "		-t: threads"
    print "		-f: dictionary file\n"
    print "example: forzabruta.py -w http://www.targetsite.com/FUZZ -t 5 -f common.txt\n"


class request_performer(Thread):
    def __init__( self,word,url):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('FUZZ',self.word)
            self.url = self.urly
        except Exception, e:
            print e

    def run(self):
        try:
            r = requests.get(self.url)
            print self.url + " - " + str(r.status_code)
            i[0]=i[0]-1 #Here we remove one thread from the counter
        except Exception, e:
                print e

def start(argv):
    banner()
    if len(sys.argv) < 5:
           usage()
           sys.exit()
    try :
        opts, args = getopt.getopt(argv,"w:f:t:")
    except getopt.GetoptError:
               print "Error en arguments"
               sys.exit()

    for opt,arg in opts :
           if opt == '-w' :
                   url=arg
           elif opt == '-f':
                   dict= arg
           elif opt == '-t':
                   threads=arg
    try:
           f = open(dict, "r")
           words = f.readlines()
    except:
           print"Failed opening file: "+ dict+"\n"
           sys.exit()
    launcher_thread(words,threads,url)

def launcher_thread(names,th,url):
    global i
    i=[]
    resultlist=[]
    i.append(0)
    while len(names):
        try:
            if i[0]<th:
                n = names.pop(0)
                i[0]=i[0]+1
                thread=request_performer(n,url)
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
