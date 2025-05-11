import socket

with socket.socket(2, 2) as s:
    for frame in input(" > "):
        while True:
            s.sendto(frame.encode(), ("127.0.0.1", 8093))
            try:
                s.settimeout(1)
                s.recvfrom(1024)
                print(frame, "Received ACK")
                break
            except socket.timeout:
                print(frame, "Timeout")
