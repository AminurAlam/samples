import socket

with socket.socket(2, 2) as s:
    msg = input(" > ")
    for window in [msg[i : 2 + i] for i in range(0, len(msg), 2)]:
        print("sending window", window)
        window = list(window)
        while window:
            for i, frame in enumerate(window):
                s.sendto(frame.encode(), ("127.0.0.1", 8093))
                try:
                    s.settimeout(1)
                    s.recvfrom(1024)
                    window.pop(i)
                except socket.timeout:
                    print(frame, "Timeout")
