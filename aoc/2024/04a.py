count = 0

def eval(a, b, c) -> bool:
    try:
        abc = text[a[0]][a[1]] + text[b[0]][b[1]] + text[c[0]][c[1]]
        if abc == "MAS":
            print(x,y)
            return True
    except IndexError: pass
    return False


with open('aoc/2024/04.txt') as file:
# with open("input") as file:
    text: list[str] = file.readlines()

    for x, line in enumerate(text):
        for y, char in enumerate(line.strip()):
            if char == "X" :
                # print(x, y)
                count += (
                    eval((x+1, y), (x+2, y), (x+3, y)) +
                    eval((x-1, y), (x-2, y), (x-3, y)) +
                    eval((x, y+1), (x, y+2), (x, y+3)) +
                    eval((x, y-1), (x, y-2), (x, y-3)) +
                    eval((x-1, y-1), (x-2, y-2), (x-3, y-3)) +
                    eval((x+1, y+1), (x+2, y+2), (x+3, y+3)) +
                    eval((x-1, y+1), (x-2, y+2), (x-3, y+3)) +
                    eval((x+1, y-1), (x+2, y-2), (x+3, y-3)) +
                    0
                )

# 2558
print(count)
# 1708
