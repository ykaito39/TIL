iptables設定例  
  
iptables -L 											#List rules  
  
iptables -A INPUT -p icmp -j ACCEPT						#icmpを許可  
iptables -A INPUT -p tcp -m tcp --dport 25565 -j ACCEPT #25565portの受信許可  
iptables -P INPUT DROP									#許可した以外の受信パケットを拒否  
iptables -P OUTPUT ACCEPT 								  
  
/etc/init.d/iptables save								#/etc/sysconfig/iptablesに保存  
