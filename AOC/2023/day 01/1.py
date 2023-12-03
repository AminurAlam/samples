import sys

collect: int = 0

for line in (sys.stdin.readlines()):
    nums: list[str] = [x for x in line if x.isdigit()]
    collect += int(nums[0] + nums[-1])
print(collect)
