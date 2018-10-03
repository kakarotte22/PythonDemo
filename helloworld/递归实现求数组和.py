def sum_array(array):
    if len(array) == 1:
        return array[-1]
    else:
        return array.pop() + sum_array(array)


lst = [1, 2, 3, 4, 5, 10]
arrsum = sum_array(lst)
print(arrsum)