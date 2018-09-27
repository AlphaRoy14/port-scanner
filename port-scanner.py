
import optparse 
from socket import *
from threading import *
'''Its a port scanner command line tool that
will scan all the comma seperated ports entered
for the target host '''

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def connScan(trgHost,trgPort):
	try:
		connSkt=socket(AF_INET,SOCK_STREAM)
		connSkt.connect((trgHost,trgPort))
		connSkt.send('hey there \r\n')
		results=connSkt.recv(100)
		print bcolors.OKGREEN+"[+]%d/tcp open"%trgPort+bcolors.ENDC
		print bcolors.OKBLUE+"[+] "+ str(results)+bcolors.ENDC
		connSkt.close()
	except:
		print bcolors.FAIL+"[-]%d/tcp closed" %trgPort+bcolors.ENDC
def portScan(trgHost,trgPorts):
	try:
		trgIp=gethostbyname(trgHost)
	except:
		print bcolors.FAIL+"[-] cannot resolve '%s' : unknown host"%trgHost+bcolors.ENDC
	try:
		trgName=gethostbyaddr(trgIp)
		print bcolors.OKGREEN+"\n[+] scan results for: "+trgName[0]+bcolors.ENDC
	except:
		print bcolors.OKGREEN+"\n[+] scan results for: "+trgIp+bcolors.ENDC

	setdefaulttimeout(1)
	for trgPort in trgPorts:
		print "Scanning port "+ trgPort
		try:

			connScan(trgHost,int(trgPort))
		except ValueError:
			print bcolors.WARNING+'specify the target port[s] seperated by '+\
			'comma as a string eg: "22, 20, 80"'+bcolors.ENDC
def main():
	parser=optparse.OptionParser("python %prog -H <target host> -p <target port>")
	parser.add_option("-H",dest='trgHost',type="string",help="specify the target host")
	parser.add_option("-p",dest="trgPort",type="string",help='specify the target port[s] seperated by\
	 comma as a string eg: "22, 20, 80"')
	(options,args)=parser.parse_args()
	trgHost=options.trgHost
	# print options.trgPort
	trgPorts=str(options.trgPort).split(', ')
	# print trgPorts
	if(trgHost==None)|(trgPorts[0]==None):
		print bcolors.FAIL+"[-] you must specify target host and port[s]."+bcolors.ENDC
		exit()
	portScan(trgHost,trgPorts)

if __name__ == '__main__':
	main()








			
