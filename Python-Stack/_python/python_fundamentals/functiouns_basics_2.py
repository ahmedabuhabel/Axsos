# 1 Countdown
def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    print(list)


# 2 Print and Return
def print_and_return(list):
    if len(list) == 2:
        print(list[0])
        return list[1]


# 3
def first_plus_length(list):
    list[0] = len(list) + 1
    return list


# 4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    newList = []

    for i in range(len(list)):
        if list[i] > list[1]:
            count = +1
            newList.append(list[i])
    print(len(newList))
    return newList


# 5
def length_and_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
