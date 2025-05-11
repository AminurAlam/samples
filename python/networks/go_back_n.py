import socket

with socket.socket(2, 2) as s:
    msg = list(input(" > "))
    while msg:
        window = msg[0:4]
        print("sending window", "".join(window))
        for frame in window:
            s.sendto(frame.encode(), ("127.0.0.1", 8093))
            try:
                s.settimeout(1)
                s.recvfrom(1024)
                msg.pop(0)
            except socket.timeout:
                print(frame, "Timeout")
                break
