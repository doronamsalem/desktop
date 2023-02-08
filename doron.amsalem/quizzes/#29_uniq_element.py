def uniq_element(arr):
    i = 0
    while arr.count(arr[i]) > 1:
        i += 1
    return arr[i]


array = [1, 1, 2, 2, 3, 3, 5, 6, 6]
array = [1, 3, 6, 1, 7, 3, 6, 8, 4, 9, 0, 0, 9, 4, 8]
print(uniq_element(array))


def uniq_element_logN(arr, len):

    if arr[len//2] == arr[len//2 + 1]:
        uniq_element_logN( arr[ len//2: arr(len) ], len//2 + 1 )

    elif arr[len//2] == arr[len//2 - 1]:
        uniq_element_logN( arr[ len//2 + 1 ], len//2 + 1 )

    else:
        return arr[len//2]





array = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
print(uniq_element_logN(array, 11))