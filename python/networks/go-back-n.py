import socket

with socket.socket(2, 2) as s:
    msg = list(input(f" > "))
    while msg:
        print(f"sending frames {''.join(msg[0:4])}")
        for frame in msg[0:4]:
            count = 0
            s.sendto(frame.encode("utf-8"), ("127.0.0.1", 8093))
            try:
                s.settimeout(1)
                s.recvfrom(1024)
                msg.pop(count)
            except socket.timeout:
                print(f"{frame}: Timeout")
                break
            count += 1
