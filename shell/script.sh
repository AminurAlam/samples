#!/usr/bin/env bash

# single line comment

: <<EOF
    multiline comment
    write anything here
EOF

### printing something to terminal

echo "hello world!"
echo "i'm printing
multiple lines"
echo "sum of 1 and 2 is $((1 + 2))"

### variables

# assigning variables
TEXT="string"
NUMBER=5
ARRAY=(foo bar baz)

# printing variables
echo $TEXT $NUMBER   # works without quotes
echo "$TEXT $NUMBER" # works with double quotes
echo '$TEXT $NUMBER' # doesn't work with single quotes
echo "
${ARRAY[0]}
${ARRAY[1]}
${ARRAY[2]}
"

# concatenating variables
NUM1=5
NUM2=7
STR="example text"

echo $NUM1+$NUM2      # adding two numbers doesn't work
echo $((NUM1 + NUM2)) # adding two numbers works now
echo $((STR + NUM1))  # concatenating str doesn't work
echo "$STR$NUM1"      # concatenating str works now

# some predefined variables in bash
echo "
user     : $USER
shell    : $SHELL
bash ver : $BASH_VERSION
home dir : $HOME
"

# unsetting variables
unset -v TEXT NUMBER

### arrays

LIST=(10 "green" "$TEXT") # defining array
LIST[4]="cookie"          # inserting item
echo "${LIST[4]}"         #indexing array
unset -v "LIST[4]"        # removing item

### arithematic operations inside $(())
#    id++, id--          variable post-increment, post-decrement
#    ++id, --id          variable pre-increment, pre-decrement
#    -, +                unary minus, plus
#    !, ~                logical and bitwise negation
#    **                  exponentiation
#    *, /, %             multiplication, division, remainder
#    +, -                addition, subtraction
#    <=, >=, <, >        comparison
#    ==, !=              equality, inequality
#    &&                  logical AND
#    ||                  logical OR
#    expr ? expr : expr  conditional operator
#    =, *=, /=, %=,
#    +=, -=, <<=,
#    >>=, &=, ^=, |=     assignment

### test conditions inside [ ]
#    -lt    less than
#    -le    less than or equal
#    -eq    equal
#    -ge    greater than or equal
#    -gt    greater than
#    -ne    not equal
#    -a     and operator
#    -o     or operator

### loops and branching

# while loop

NUM=1
while [ $NUM -le 10 ]; do
    ((++NUM))
done

# until loop

NUM=1
until [ $NUM -gt 10 ]; do
    ((++NUM))
done

# for loop

for NUM in {1..10}; do
    echo -n
done

for ((NUM = 1; NUM < 10; ++NUM)); do
    echo -n
done

for name in a b c; do
    echo -n "$name, "
done

for file in *; do
    touch "$file"
done

# if statement

if [ "$CONDITION" = true ]; then
    echo -n
elif [ "$CONDITION" = false ]; then
    echo -n
else
    echo -n
fi

# select

echo -e "\n\nselect one of the following:"

select name in red blue green; do
    echo -e "you selected $name \n"
    break
done

# match case is too complicated :(

### function

# defining function

function length() {
    echo -e "'$1' is ${#1} characters long"
}

function add() {
    ((RESULT = $1 + $2))
    echo -e "sum of $1 and $2 is $RESULT"
}

# calling function
length "river"
add 5 7

# deleting function
unset -f length
unset -f add

### file handling

touch chat.txt        #creating a file
cp chat.txt chat2.txt #copying a file
mv chat.txt chat2.txt #moving a file
rm chat2.txt          #deleting a file

echo "how are you?" >chat.txt #inserting text
echo "im good" >>chat.txt     #appending text
cat chat.txt                  #printing file's content
