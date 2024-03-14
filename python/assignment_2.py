def check_prime():
    print("\n### check if given number is prime")
    num = int(input("enter a number: "))

    for i in range(2, num//2):
        if num % i == 0:
            print(num, "is NOT prime")
            exit()

    print(num, "is prime")

def check_armstrong():
    print("\n### check if given number armstrong")
    cpy = num = int(input("enter a number: "))
    sum = 0

    while num:
        sum += (num % 10) ** 3
        num //= 10

    if sum == cpy:
        print("arm")
    else:
        print("NOT arm")

def calc_fact():
    print("\n### calc factorial of a number")
    num = int(input("enter a number: "))
    fact = 1

    for i in range(2, num+1):
        fact *= i

    print(f"factorial of {num} is {fact}")

def find_series():
    num = int(input("enter a number: "))
    sum = 0

    for i in range(num):
        sum += 1/((i*2)+1)

    print(sum)

def fib():
    num = int(input("enter a number: "))
    n1, n2 = 0, 1

    for _ in range(num):
        print(n1 + n2)
        n1, n2 = n2, n1 + n2


# check_prime()
# check_armstrong()
# calc_fact()
# find_series()
# fib()
