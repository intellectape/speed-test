import sys
import os
import socket
import time


if len(sys.argv) != 3:
    print("python client.py <server address> <server port>")
    exit(1)

initialPacket = 10 * 1024
sendingPacket = 1 * 1024 * 1024
handshake = 20
ACK = 41

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host, port))

def packetCreation(packetsize):
    return bytearray(os.urandom(packetsize))

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

        rtt = end_time -start_time
        up_speed = (len(packet) * 1000 * 8) / rtt
        return up_speed
    except:
        print("An Exception has occurred in the code.")
        return 0

def download():
    global s, sendingPacket
    try:
        s.send(bytes(handshake))

        start_time = int(round(time.time() * 1000))

        receive_packet = s.recv(sendingPacket)

        end_time = int(round(time.time() * 1000))

        rtt = end_time - start_time
        down_speed = (len(receive_packet) * 1000 * 8) / rtt
        return down_speed
    except:
        print("An Exception has occurred in the code.")
        return 0

def main():
    global initialPacket, sendingPacket, s
    down_speed = download()
    up_speed = upload()

    print("Download Speed: " + str(down_speed/ (1024 * 1024)) + " Mbits/sec")
    print("Upload Speed: " + str(up_speed / (1024 * 1024)) + " Mbits/sec")
    s.close

if __name__ == "__main__":
    main()