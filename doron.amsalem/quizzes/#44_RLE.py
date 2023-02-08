def RLE(string):
    cnt = 1
    RLE_string = ""
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            cnt += 1
            continue
        elif cnt > 1:
            RLE_string += str(cnt) + string[i]
        else:
            RLE_string += string[i]
        cnt = 1

    if cnt > 1:
        RLE_string += str(cnt) + string[len(string) - 1]
    else:
        RLE_string += string[len(string)]

    return RLE_string


print(RLE("WWWWEERRRFGKKK"))