def reverse_string1(string):
    return string[::-1]


def reverse_string2(string):
    s = ""
    for i in range(len(string) -1, -1, -1):
        s += string[i]
    return s


print(reverse_string1("doron"))
print(reverse_string2("doron"))
sr = "asdfg"