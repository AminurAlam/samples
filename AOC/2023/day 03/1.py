import sys

collect: int = 0
ignore: int = 0
streak: bool = False
lines = sys.stdin.readlines()

def get_num(c: int, line: str) -> dict[str, int]:
    num = ''
    for next_char in line[c:]:
        if next_char.isdigit(): num += next_char
        else: break

    return {"num": int(num), "start": c, "end": c + len(num) - 1}

def check_symbol(char: str) -> bool:
    if char != '.' and not char.isdigit():
        return True
    return False

def check_leftmost(x, y):
    print("left c for: ", lines[y][x])
    if 0 < x and 1 < y and check_symbol(lines[y-1][x-1]): return True
    if 0 < x and check_symbol(lines[y][x-1]): return True
    if 0 < x and y+1 < len(lines) and check_symbol(lines[y+1][x-1]): return True
    return False

def check_rightmost(x, y):
    print("right c for: ", lines[y][x])
    if x < lim and 1 < y and check_symbol(lines[y-1][x+1]): return True
    if x < lim and check_symbol(lines[y][x+1]): return True
    if x < lim and y+1 < len(lines) and check_symbol(lines[y+1][x+1]): return True
    return False

def check_updown(piece: dict[str, int], y: int) -> bool:
    for x in range(piece["start"], piece["end"]+1):
        print("updown c for: ", lines[y][x])
        if 1 < y and check_symbol(lines[y-1][x]): return True
        if y+1 < len(lines) and check_symbol(lines[y+1][x]): return True

    return False


for l, line in enumerate(lines):
    line = line.strip()
    lim = len(line[0]) + 1
    for c, char in enumerate(line):
        if ignore:
            ignore -= 1
            continue

        if char.isdigit():
            piece = get_num(c, line) # ......piece....piece.......
            ignore = piece["end"] - piece["start"] # + 1
            if check_updown(piece, l) or check_leftmost(piece["start"], l) or check_rightmost(piece["end"], l):
                print(piece, l)
                collect += piece["num"]

print(collect)
