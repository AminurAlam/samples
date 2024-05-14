# Input n numbers in a bit then print the list in the reverse order
# Input 10 numbers in a bit and print the first 3 and last 3 numbers
# Input in numbers in n bit then print max, min, and average of the list.


def rev_list():
    size = int(input("enter size of list: "))
    array = []

    for _ in range(size):
        item = int(input("enter item: "))
        array.append(item)

    array.reverse()
    print(array)


def head_tail():
    array = []

    for _ in range(10):
        item = int(input("enter item: "))
        array.append(item)

    print(array[0:3])
    print(array[7:11])


def min_max():
    size = int(input("enter size of list: "))
    array = []

    for _ in range(size):
        item = int(input("enter item: "))
        array.append(item)

    print("smallest item is:", min(array))
    print("biggest item is:", max(array))
    print("average is:", sum(array) / len(array))


# rev_list()
# head_tail()
# min_max()
