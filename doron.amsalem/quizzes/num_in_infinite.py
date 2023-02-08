def binary_search(num, arr, start, stop, mid):
    if arr[mid] == num:
        return mid
    else:
        if arr[mid] > num:
            return binary_search(num, arr, start, mid, int(start + (mid - start) / 2) )
        else:
            return binary_search(num, arr, mid, stop, int(mid + (stop - mid) / 2) )


# find the range the num exist in
def find_num(num, arr):
    i = 1
    if arr[0] == num:
        return 0
    else:
        while num > arr[i]:
            last_i = i
            i *= 2
        return binary_search(num, arr, last_i, i, int(last_i + (i - last_i) / 2))


arr = []
for x in range(-2, 1000):
    arr.append(x)
print(find_num(80, arr))
