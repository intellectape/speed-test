import sys
import os
import socket


if len(sys.argv) != 3:
    print("python client.py <server address> <server port>")
    exit(1)

initialPacket = 10 * 1024
sendingPacket = 1 * 1024 * 1024
handshake = 20
ACK = 41

host = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port))

def packetCreation(packetsize):
    return bytearray(os.urandom(packetsize))

def main():
    global initialPacket, sendingPacket, s
    s.listen(5)
    print("Server Up!")
    c, address = s.accept()
    
    while True:    
        print("Connected to :", address)
        packet = packetCreation(sendingPacket)
        test_status = clientDownload(c, packet)
        
        if not test_status:
            print("Executiong Failed: Client Download Test")
        
        clientUpload(c)
        print("Test Completed!")
        print("#####################################")
        s.close()

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


if __name__ == "__main__":
    main()