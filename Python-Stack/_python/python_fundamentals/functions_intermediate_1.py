import random


def randInt(min=0, max=100):
    if min > max:
        return False

    num = random.random() * (max - min) + min
    return round(num)


print(randInt())  # s between 0 to 100
print(randInt(max=50))  # s between 0 to 50
print(randInt(min=50))  # s between 50 to 100
print(randInt(min=50, max=500))  # s between 50 and 500
