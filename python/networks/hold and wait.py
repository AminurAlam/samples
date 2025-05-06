import socket

with socket.socket(2, 2) as s:
    frame = 0
    while True:
        msg = input(f"{frame} > ")
        s.sendto(msg.encode("utf-8"), ("127.0.0.1", 8093))
        try:
            s.settimeout(1)
            s.recvfrom(1024)
            print(f"Received ACK")
        except socket.timeout:
            print(f"{frame}: Timeout")
        frame += 1
