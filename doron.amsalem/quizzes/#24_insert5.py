def insert5(num):
    string_num = str(num)
    for i in range(len(string_num)):
        if int(string_num[i]) < 5:
            return int(string_num.replace(string_num[i], "5", 1))


if __name__ == "__main__":
    n = 8675441
    print(insert5(n))
    n = 22222
    print(insert5(n))
