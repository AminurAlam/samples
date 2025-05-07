import random
import socket

with socket.socket(2, 2) as s:
    s.bind(("127.0.0.1", 8093))
    while True:
        data, sender = s.recvfrom(1024)
        if not random.randint(0, 3):
            continue
        print(data.decode("utf-8"))
        s.sendto("ok".encode("utf-8"), sender)
