import socket

with socket.socket(2, 2) as s:
    frame = 0
    while True:
        msg = input("%d > " % frame)
        s.sendto(msg.encode("utf-8"), ("127.0.0.1", 8093))
        try:
            s.settimeout(1)
            s.recvfrom(1024)
            print("Received ACK")
        except socket.timeout:
            print(frame, "Timeout")
        frame += 1
