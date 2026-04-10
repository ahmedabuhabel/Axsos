# 1
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list


# 2
def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list[len(list) - 1] = count
    return list


# 3
def sum_total(list):
    sum = 0
    for i in list:
        sum += i
    return sum


# 4
def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)


# 5
def length(list):
    count = 0
    for i in list:
        count += 1
    return count


# 6
def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min


# 7
def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


# 8
def ultimate_analysis(list):
    dict = {
        "sumTotal": sum_total(list),
        "average": average(list),
        "minimum": minimum(list),
        "maximum": maximum(list),
        "length": length(list),
    }
    return dict


# 9
def reverse_list(list):
    left = 0
    right = len(list) - 1
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    return list
