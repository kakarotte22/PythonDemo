def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle_value = arr[0]
        small = [i for i in arr[1:] if i <= middle_value]
        big = [i for i in arr[1:] if i > middle_value]
        return qsort(small) + [middle_value] + qsort(big)


print(qsort([10, 5, 4, 7, 20]))