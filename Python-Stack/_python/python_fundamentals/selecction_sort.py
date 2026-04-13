def selection_sort(arr):
    for j in range(0, len(arr) - 1):
        min_index = j
        for i in range(j + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        if min_index != j:
            arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr


print(selection_sort([20, 6, 11, 7, 6, 3]))
""" [20, 6, 11, 7, 6, 3]
j=0  min= 0 i=1 arr[i] = 6 arr[min]= 20==> min=1
j=0  min= 1 i=2 arr[i] = 11 arr[min]= 6
j=0  min= 1 i=3 arr[i] = 7 arr[min]= 6
j=0  min= 1 i=4 arr[i] = 6 arr[min]= 6
j=0  min= 1 i=5 arr[i] = 3 arr[min]= 6 ==> min=5 eol
j=0  min= 5 i=5 arr[i] = 3 arr[min]= 3 ==> swap arr[j] arr[min]

[3, 6, 11, 7, 6, 20]
j=1  min= 1 i=2 arr[i] = 11 arr[min]= 6
j=1  min= 1 i=3 arr[i] = 7 arr[min]= 6
j=1  min= 1 i=4 arr[i] = 6 arr[min]= 6
j=1  min= 1 i=5 arr[i] = 20 arr[min]= 6

[3, 6, 11, 7, 6, 20]
j=2  min= 2 i=3 arr[i] = 7 arr[min]= 11 ==> min=3
j=2  min= 3 i=4 arr[i] = 6 arr[min]= 7 ==> min =4
j=2  min= 4 i=5 arr[i] = 20 arr[min]= 6 eol j=2  min= 4 i=5 arr[i] = 20 arr[min]= 6 ==> swap arr[j] arr[min]
[3, 6, 6, 7, 11, 20] """


