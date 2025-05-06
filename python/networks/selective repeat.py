import socket

with socket.socket(2, 2) as s:
    msg = input(f" > ")
    msg = [msg[i : 2 + i] for i in range(0, len(msg), 2)]
    print(msg)
    while msg:
        print(f"sending frames {msg[0]}")
        count = 0
        for frame in msg[0]:
            s.sendto(frame.encode("utf-8"), ("127.0.0.1", 8093))
            try:
                s.settimeout(1)
                s.recvfrom(1024)
                count += 1
            except socket.timeout:
                print(f"{frame}: Timeout")
                break
        if count == len(msg[0]):
            msg.pop(0)
