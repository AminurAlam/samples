import sys

collect: int = 0

for n, line in enumerate(sys.stdin.readlines(), start=1):
    data = {"red": 0, "blue": 0, "green": 0}

    for part in line.split(': ')[1].split('; '):
        for aaa in part.split(', '):
            pair = aaa.split()
            data[pair[1]] = max(data[pair[1]], int(pair[0]))
    collect += data['red'] * data['blue'] * data['green']

print(collect)
