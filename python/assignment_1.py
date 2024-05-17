def check_max():
    print("\n### input two numbers and check which one in maximum")
    a = int(input("enter a: "))
    b = int(input("enter b: "))

    if a > b:
        print(a, "is bigger")
    else:
        print(b, "is bigger")


def odd_or_even():
    print("\n### check if given number is odd or even")
    num = int(input("enter a number: "))

    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


def find_sum():
    print("\n### find sum of digits of a number")
    num = int(input("enter a number: "))
    sum = 0

    while num:
        sum += num % 10
        num = num // 10

    print("sum is:", sum)


def check_palindrome():
    print("\n### check if a number is palindrome or not")
    num = int(input("enter a number: "))
    cpy = num
    rev = 0

    while num:
        rev = (rev * 10) + (num % 10)
        num = num // 10

    if cpy == rev:
        print(cpy, "is a palindrome")
    else:
        print(cpy, "is a NOT palindrome")


def star_tree():
    print("\n### print a star tree")
    num = int(input("enter a number: "))

    for i in range(num + 1):
        print("*" * i)


# check_max()
# odd_or_even()
# find_sum()
# check_palindrome()
# star_tree()
