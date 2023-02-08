# interview by sara
def rotate_left(ls):
    """get list and rotate it left"""
    temp = ls[0]
    ls2 = ls[slice(1, None)]
    ls.clear()
    for i in ls2:
        ls.append(i)
    ls.append(temp)


if __name__ == "__main__":
    ls = [1, 2, 3, 4, 5]
    rotate_left(ls)
    print(ls)
