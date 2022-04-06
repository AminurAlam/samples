#single line comment
"""
multi line comment
write anything here
"""




###printing something

print("hello world!")
print("""i'm printing
multiple lines""")
print(f"sum of 1 and 2 is {1+2}")





###variables and data

#assigning variables
text = "string"                     # string
number = 5                          # integer
decimal = 2.72                      # folating point

#printing variables
print("text, number")           # doesn't work with quotes
print(f"{text}, {number}")      # works with function string
print(text, number)             # works without quotes

#concatenating variables
try:    print(text + number)          # doesn't work
except: print(text + str(number))     # works now

#lists, tuples, and dictionary
items = ["string", 5, 2.72, text]   # list
items2 = ("string", 5, 2.72, text)  # tuple
items3 = {                          # dictionary
    "text": "string",
    "number": 5,
    "decimal": 2.72,
    "items": [1, "value"],
    "items": {1:"a"},
    "variable": text
        }

print(items[0], items[1], items[2])
print(items2[0], items2[1], items2[2])
print(
        items3['text'],
        items3['number'],
        items3['decimal']
        )

#some predefined variables/built-in scope
print(f"""
    name : {__name__}
    dir  : {dir()}
    """)




###loops

#while loop
n = 0
while n < 10:
    n += 1
    print(n, end=", ")

#for loop
for n in range(1, 11):
    print(n, end=", ")




###function

#defining function

def findLength(data):
    print(f"'{data}' is {len(data)} characters long")

def add(num1, num2):
    result = num1 + num2
    print(f"sum of {num1} and {num2} is {result}")
    return result

#calling function
findLength("river")
add(5, 7)
