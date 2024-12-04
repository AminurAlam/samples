set state 1

for inst in (rg --only-matching 'do\(\)|don\'t\(\)|mul\(\d+,\d+\)' aoc/2024/03.txt)
    if [ "$inst" = "do()" ]
        set state 1
    else if [ "$inst" = "don't()" ]
        set state 0
    else if [ "$state" = 1 ]
        string replace , '*' "$inst" | string replace 'mul' '+'
    end
end | math
