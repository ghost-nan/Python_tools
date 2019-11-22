#coding=utf-8
import socket
 
target_host = "127.0.0.1"
target_port = 1234
 
#建立一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
#发送一些数据
client.sendto("This is an UDP client",(target_host,target_port))
 
#接收一些数据
data, addr = client.recvfrom(4096)
 
print data
print addr
