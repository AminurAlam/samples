# 1) create a folder
import os

os.mkdir("test")

# 2)create a file inside
with open("test/file", "w") as file:
    file.write("")

# 3) write your address in the file.
with open("test/file", "w") as file:
    file.write("address\n")

# 4) read the file
with open("test/file", "r") as file:
    print(file.read())

# 5) Modify the file and your phone number.
with open("test/file", "a") as file:
    file.write("+00 12345\n")
