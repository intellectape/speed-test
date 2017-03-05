import sys
import socket

# Using slow start approach for getting faster results

if len(sys.argv) != 3:
    print("python client.py <server address> <server port>")
    exit(1)

initialPacket = 50 * 1024
sendingPacket = 5 * 1024 * 1024

s = socket.socket() 
host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host, port))

print(s.recv(1024))
s.close

def main():
    global initialPacket, sendingPacket
    

    return True

if __name__ == "__main__":
    main()