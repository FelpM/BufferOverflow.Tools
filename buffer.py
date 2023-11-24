import socket
from struct import pack

IP = "192.168.1.2"
port = 21449

def fuzz():
    try:
        for i in range(0,12000,500):
            buffer = b"A"*i
            print("Fuzzing %s bytes" % i)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, port))
            s.send(buffer)
            breakpoint()
            s.close()
    except:
        print("Could not establish a connection")

fuzz()
