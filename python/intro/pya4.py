# 1) Input string and reverse it using loop.
# 2) Input a string and input a substring check if the substring is present in the string.
# 3) Input a password and check
# i) the length should be at lest 6 characters
# ii) there should be at least one digit and one special character form.
# 4) Input a string and check if it is palindrome or not.


def rev_str():
    line = input("enter string: ")
    for i in range(len(line), 0, -1):
        print(line[i - 1], end="")


def sub_search():
    sup = input("enter string: ")
    sub = input("enter sub-string: ")

    if sup.find(sub) > -1:
        print(sub, "is present in", sup)
    else:
        print(sub, "is not present in", sup)


def secure():
    passwd = input("enter password: ")
    digit = False
    special = False

    for num in range(10):
        if str(num) in passwd:
            digit = True

    for char in ["?", "!", "*"]:
        if char in passwd:
            special = True

    if len(passwd) < 6:
        print("password is too short")
    if not digit:
        print("password doesnt have any digits")
    if not special:
        print("password doesnt have any special characters")


def palindrome():
    string = input("enter a string: ")

    if string == string[::-1]:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")


# rev_str()
# sub_search()
# secure()
# palindrome()
