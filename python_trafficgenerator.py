import socket
import random
import time

bufferSize  = 1024
serverAddressPort   = ("127.0.0.1", 7501)


print('this program will generate some test traffic for 2 players on the red ')
print('team as well as 2 players on the green team')
print('')

# Create datagram socket
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# counter number of events, random player and order
def generateTraffic(red1, red2, green1, green2, counter):
	for i in range(counter):
		if random.randint(1,2) == 1:
			redplayer = red1
		else:
			redplayer = red2

		if random.randint(1,2) == 1:
			greenplayer = green1
		else: 
			greenplayer = green2	

		if random.randint(1,2) == 1:
			message = redplayer + ":" + greenplayer
		else:
			message = greenplayer + ":" + redplayer

		print(message)

		UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
		time.sleep(random.randint(1,3))