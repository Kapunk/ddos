import socks
import socket
import os

def renewTorIdentity(self, passAuth):
	try:
		resp = os.system("sudo /etc/init.d/tor restart")
		print resp
		socks.set_default_proxy(socks.SOCKS4, "127.0.0.1", 9050)
		socket.socket = socks.socksocket
		s = socket.socket()
		s.connect(('localhost', 9051))
		s.send('AUTHENTICATE "{0}"\r\n'.format(passAuth))
		resp = s.recv(1024)
		if resp.startswith('250'):
			s.send("signal NEWNYM\r\n")
			resp = s.recv(1024)
			if resp.startswith('250'):
				print "Identity renewed"
			else:
				print "response 2:", resp
		else:
			print "response 1:", resp
	except Exception as e:
		print "Can't renew identity: ", e 

def checkForTor():
	try:
		resp = os.system("ps aux | grep -w [t]or")
		if resp == 0:
			print "Tor instalado"
			return 0
		else:
			print "Tor No instalado"
			return 1
	except Exception as e:
		print "Excepcion de Tor: ", e

def installTor():
	resp = os.system("sudo apt-get install tor")


import urllib2

if checkForTor()==0:
	for i in [0, 1, 2]:
#		renewTorIdentity("a",123)
		print(urllib2.urlopen('http://icanhazip.com').read())
else:
	installTor()
