import sys
import os
import socket
import time


if len(sys.argv) != 3:
    print("python client.py <server address> <server port>")
    exit(1)

# Variables for data packet size and handshake, ACK for establishing communication over the network
initialPacket = 1024
sendingPacket = 10 * 1024
handshake = 20
ACK = 41

# Initializing the socket for the Client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host, port))

# Function to eliminate slow start problem of TCP
def slowStartEnd():
    global s
    try:
        packet = packetCreation(initialPacket)
        s.send(packet)
        data = s.recv(initialPacket)
    except:
        print("Exception have occurred in the code!")
        exit(0)

# Function to create Packets at random
def packetCreation(packetsize):
    return bytearray(os.urandom(packetsize))

# Function to test Upload Functionality fo the client
def upload():
    global ACK, s
    try:
        packet = packetCreation(sendingPacket)
        
        start_time = int(round(time.time() * 1000))
        s.send(packet)
        flag = s.recv(ACK)

        if not flag:
            print("No acknowledgment for upload received.")
            exit(0)

        end_time = int(round(time.time() * 1000))

        # rtt is the trip time from one side
        rtt = end_time -start_time
        
        # if the connection is on local network, then to avoid error in upload time
        if rtt == 0:
            rtt = 1
        up_speed = (len(packet) * 1000 * 8) / rtt
        return up_speed
    except:
        print("An Exception has occurred in the code.")
        return 0

# Function to test Download Functionality of the Client
def download():
    global s, sendingPacket
    try:
        s.send(bytes(handshake))
        print("Sending handshake to the server signalling readiness for receiving data.")

        start_time = int(round(time.time() * 1000))

        receive_packet = s.recv(sendingPacket)

        end_time = int(round(time.time() * 1000))

        print("Received packet.")

        # rtt is the trip time from one side
        rtt = end_time - start_time

        # if the connection is on local network, then to avoid error in download time
        if rtt == 0:
            rtt = 1
        down_speed = (len(receive_packet) * 1000 * 8) / rtt
        return down_speed
    except:
        print("An Exception has occurred in the code.")
        return 0

def main():
    global initialPacket, sendingPacket, s
    
    slowStartEnd()
    down_speed = download()
    up_speed = upload()

    print("Download Speed: " + str(down_speed/ (1024 * 1024)) + " Mbits/sec")
    print("Upload Speed: " + str(up_speed / (1024 * 1024)) + " Mbits/sec")
    s.close

if __name__ == "__main__":
    main()