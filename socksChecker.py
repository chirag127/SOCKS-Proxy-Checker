#Developed by TheBeast808
import socket
import Queue
import threading
import time
from struct import *
class ThreadChecker(threading.Thread):
	def __init__(self, queue, timeout):
		self.timeout = timeout
		self.q = queue
		threading.Thread.__init__(self)
	def isSocks4(self, host, port, soc):
		ipaddr = socket.inet_aton(host)
		packet4 = "\x04\x01" + pack(">H",port) + ipaddr + "\x00"
		soc.sendall(packet4)
		data = soc.recv(8)
		if(len(data)<2):
			# Null response
			return False
		return False if data[0] != "\x00" else data[1] == "\x5A"
	def isSocks5(self, host, port, soc):
		soc.sendall("\x05\x01\x00")
		data = soc.recv(2)
		if(len(data)<2):
			# Null response
			return False
		return False if data[0] != "\x05" else data[1] == "\x00"
	def getSocksVersion(self, proxy):
		host = proxy.split(":")[0]
		try:
			port = int(proxy.split(":")[1])
			if port < 0 or port > 65536:
				print "Invalid: " + proxy
				return 0
		except:
			print "Invalid: " + proxy
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(self.timeout)
		try:
			s.connect((host, port))
			if(self.isSocks4(host, port, s)):
				s.close()
				return 5
			elif(self.isSocks5(host, port, s)):
				s.close()
				return 4
			else:
				("Not a SOCKS: " + proxy)
				s.close()
				return 0
		except socket.timeout:
			print "Timeout: " + proxy
			s.close()
			return 0
		except socket.error:
			print "Connection refused: " + proxy
			s.close()
			return 0
	def run(self):
		while True:
			proxy = self.q.get()
			version = self.getSocksVersion(proxy)
			if version == 5 or version == 4:
				print "Working: " + proxy
				socksProxies.put(proxy)
			self.q.task_done()
class ThreadWriter(threading.Thread):
	def __init__(self, queue, outputPath):
		self.q = queue
		self.outputPath = outputPath
		threading.Thread.__init__(self)
	def run(self):
		while True:
			toWrite = self.q.qsize()
			with open(self.outputPath, 'a+') as outputFile:
				for _ in xrange(toWrite):
					proxy = self.q.get()
					outputFile.write(proxy + "\n")
					self.q.task_done()
			time.sleep(10)
checkQueue = Queue.Queue()
socksProxies = Queue.Queue()
with open(raw_input("Proxy list: "), 'r') as inputFile:
	outputPath = raw_input("Output file: ")
	threads = int(raw_input("Number of threads: "))
	timeout = int(raw_input("Timeout(seconds): "))
	for line in inputFile:
		checkQueue.put(line.strip('\n'))
for _ in xrange(threads):
	t = ThreadChecker(checkQueue, timeout)
	t.setDaemon(True)
	t.start()
	time.sleep(.25)
wT = ThreadWriter(socksProxies, outputPath)
wT.setDaemon(True)
wT.start()
checkQueue.join()
socksProxies.join()