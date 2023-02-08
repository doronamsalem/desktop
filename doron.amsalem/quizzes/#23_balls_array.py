def balls( arr ):
    arr_len = len(arr)
    green = arr.count("g")
    red = arr.count("r")
    yellow = arr_len - green - red
    arr.clear()

    while arr_len > 0:
        if green > 0:
            arr.append("G")
            green -= 1
        elif yellow > 0:
            arr.append("Y")
            yellow -= 1
        elif red > 0:
            arr.append("R")
            red -= 1
        arr_len -= 1


arr = ["g", "y", "r", "g", "g", "r", "y", "y"]
balls(arr)
print(arr)