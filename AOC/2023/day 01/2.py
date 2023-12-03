import sys

collect: int = 0

for line in (sys.stdin.readlines()):
    for num, al in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], start=1):
        line: str = line.replace(al, al + str(num) + al)
    nums: list[str] = [x for x in line if x.isdigit()]
    collect += int(nums[0] + nums[-1])
print(collect)
