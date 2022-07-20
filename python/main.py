# single line comment
"""
multi line comment
write anything here
"""




### printing something ###

print("hello world!")
print("""i am printing
multiple lines""")
print(f"sum of 1 and 2 is {1+2}")




### variables and data ###

# assigning variables
text = "string"             # string
number = 5                  # integer
decimal = 2.72              # folating point

# printing variables
print("text, number")       # doesn't work with quotes
print(f"{text}, {number}")  # works with function string
print(text, number)         # works without quotes

# list and dictionary
items = ["string", 5, 2.72, text]   # list
items3 = {                          # dictionary
    "text": "string",
    "number": 5,
    "decimal": 2.72,
    "items1": [1, "value"],
    "items2": {1: "a"},
    "variable": text
}

print(items[0], items[1], items[2])
print(
        items3['text'],
        items3['number'],
        items3['decimal']
        )

# some predefined variables/built-in scope
print(f"""
    name : {__name__}
    dir  : {dir()}
    """)




### string manipulation ###
text = "hello world, this is a line"
print(
    len(text),                # length -> 27
    text[6:17],               # splicing -> "world, this"
    text + " ! " + str(2),    # concatenating
    sep="\n"
)




### loops ###

# while loop
n = 0
while n < 10:
    n += 1
    print(n, end=", ")

# for loop
for n in range(1, 11):
    print(n, end=", ")




### statements ###

# if/else
if True:
    print("true")
elif False:
    print("false")
else:
    print("none")

var = "true string" if True else "false string"

# try/except
try:
    print()
except Exception as error:
    print(error)




### function ###

# defining function

def findLength(data):
    print(f"'{data}' is {len(data)} characters long")

def add(num1, num2):
    result = num1 + num2
    print(f"sum of {num1} and {num2} is {result}")
    return result

# calling function
findLength("river")
add(5, 7)

# anonymous function
lambda: 5
lambda num: num + 5
func = lambda num: num + 5

func(7)

# args/kwargs
def foo(*args):
    # prints a tuple with all argumets
    print(args)

foo(1, 2, "three")  # (1, 2, "three")


def bar(**kwargs):
    # prints dict with variables as key
    print(kwargs)

bar(a="one", b="two")  # {"a": "one", "b": "two"}


def foo2(a, b):
    return a + b

tab = [5, 7]
foo2(*tab)


def bar2(a, b):
    return a + b

obj = {"a": 5, "b": 7}
bar2(**obj)




### cryptography ###

# base64
import base64

msg = "super secret text"

enc_msg = base64.b64encode(msg.encode())
print("encoded message:", enc_msg.decode())

dec_msg = base64.b64decode(enc_msg)
print("decoded message:", dec_msg.decode())
