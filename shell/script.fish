# single line comment

: '
multiline comment
write anything here
'


### printing something to terminal

echo "hello world!"
echo "i'm printing
multiple lines"
echo "sum of 1 and 2 is $(math 1 + 2)"


### variables

# assigning variables
set -l TEXT string
set -l NUMBER 5
set -l ARRAY first 73 last

# printing variables
echo $TEXT $NUMBER # works without quotes
echo "$TEXT $NUMBER" # works with double quotes
echo '$TEXT $NUMBER' # doesn't work with single quotes
echo "
$ARRAY[1]
$ARRAY[2]
$ARRAY[3]
"

# concatenating variables
set -l NUM1 5
set -l NUM2 7
set -l STR "example text"

echo $NUM1 + $NUM2 # adding two numbers doesn't work
math $NUM1 + $NUM2 # adding two numbers works now

math $STR + $NUM1 # joining str and num doesn't work
echo "$STR$NUM1" # joining str and num works now

# some predefined variables in fish
echo "
user  : $USER
shell : $SHELL
home  : $HOME
"

# unsetting variables
set -e TEXT
set -e NUMBER


### arrays
set -l LIST 10 green $TEXT # creating
set -l LIST[4] cookie # adding item
echo $LIST[4] # accessing item
set -e LIST[4] # removing item


### arithematic operations using math command
# +      for addition
# -      for subtraction
# * or x for multiplication. * is the glob character and needs to
#        be quoted or escaped, x needs to be followed by
#        whitespace or it looks like 0x hexadecimal notation.
# /      for division
# ^      for exponentiation
# %      for modulo
# ( or ) for grouping. These need to be quoted or escaped because
#        () denotes a command substitution.
# They are all used in an infix manner - 5 + 2, not + 5 2.


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
set NUM 1
while [ "$NUM" -le 10 ]
    set NUM (math $NUM + 1)
end

# for loop
for n in (seq 10)
    echo "$n"
end

for name in a b c
    echo -n "$name, "
end

for file in *
    echo "$file"
end

# if statement
if [ $CONDITION ]
    echo true
else if [ ! $CONDITION ]
    echo false
else
    echo maybe
end

# switch case
read COLOR -fP "select one of the following:
      red, blue, green"

switch "$COLOR"
    case red
        echo "you picked red"
    case blue
        echo "you picked blue"
    case green
        echo "you picked green"
    case '*'
        echo unrecognized
end


### function

# defining function
function length
    echo $argv is (string length "$argv") characters long
end

function add
    echo sum of $argv[1] and $argv[2] is (math 1 + 2)
end

# calling function
length river
add 5 7

# deleting function
functions -e length
functions -e add
