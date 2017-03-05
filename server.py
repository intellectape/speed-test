import sys
import os
import socket


if len(sys.argv) != 3:
    print("python client.py <server address> <server port>")
    exit(1)

initialPacket = 1024
sendingPacket = 10 * 1024 
handshake = 20
ACK = 41

# Initializing the socket for the Server
host = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port))
s.listen(5)
print("Server Up!")
c, address = s.accept()

# Function to eliminate slow start problem of TCP
def slowStartEnd():
    global c
    try:
        data = c.recv(initialPacket)
        packet = packetCreation(initialPacket)
        c.send(packet)
    except:
        print("Exception have occurred in the code!")
        exit(0)

# Function to create Packets at random
def packetCreation(packetsize):
    return bytearray(os.urandom(packetsize))

def clientUpload(client):
    global sendingPacket

    data = client.recv(sendingPacket)

    if not data:
        print("Execution Failed: Client Upload Test ")
        exit(0)
    client.send(bytes(ACK))
    print("Upload Acknowledgment sent.")

def clientDownload(client, packet):

    hands = client.recv(handshake)
    if not hands:
        print("No Handshake from Client.")
    
    client.send(packet)
    print("Packet sent to Client.")
    return True

def main():
    global initialPacket, sendingPacket, s, c, address
    slowStartEnd()
    
    while True:    
        print("Connected to :", address)
        packet = packetCreation(sendingPacket)
        test_status = clientDownload(c, packet)
        
        if not test_status:
            print("Execution Failed: Client Download Test")
        
        clientUpload(c)
        print("Test Completed!")
        print("#####################################")
        s.close()

if __name__ == "__main__":
    main()