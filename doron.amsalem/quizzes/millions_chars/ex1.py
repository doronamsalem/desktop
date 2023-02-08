from max_min import max_min_dictionary

def max_occurrence(char, dic_occurrenes = {}):
    if char != '0':
        if char in dic_occurrenes.keys():
            last_occ = dic_occurrenes.pop(char)
            dic_occurrenes.update({char: last_occ + 1})
        else:
            dic_occurrenes.update({char: 1})
    #    dic_occurrenes.get(char, 0)+1           maybe can replace the if else
    else:
        # gives the key of the char with the biggest occurrences, a & b not mather
        max_char, occurre, a, b = max_min_dictionary(dic_occurrenes)
        print("max value's key:{} appeared {}".format(max_char, occurre))
        dic_occurrenes.clear()


if __name__ == "__main__":
    print("enter char(or exit):")
    char = input()
    while char != "exit":
        max_occurrence(char)
        print("enter char(or exit):")
        char = input()

"""from max_min import max_min_dictionary
from occurrense import occurrence

def max_occurrence(char, lis = []):
    if char != '0':
        lis.append(char)
    else:
        dic_occurrenes = occurrence("aaaabccccc")
        max_char, max_occurre, min, occ = max_min_dictionary(dic_occurrenes)
        print("max value's key:{} appeared {}".format(max_char, max_occurre))
        lis.clear()"""