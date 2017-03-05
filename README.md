# speed-test coding assignment

a) A server which acts as one of the end point. Assume this is the server piece for the speedtest.net, except you don't pick location. The server should be standalone and should take an IP & port as input on which it will listen. Say 
--server-ip : specify the ip address on which the server listens
--server-port: port on which the server will bind to.

b) A cli which acts as the client. The cli should have the following command line options
--server-ip : specify the server ip address
--server-port: server port.
The output should show a summary:
Download Speed: in Bits/sec
Upload Speed: in Bits/sec
