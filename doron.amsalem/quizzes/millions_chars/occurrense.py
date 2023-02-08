# interview by basheer
def occurrence(str):
    """gets string and return dictionary with letter : number of occurrence """
    dict_occurrence = {}
    str.replace(" ", "")
    for char in str:
        dict_occurrence.update({char: str.count(char)})
    return dict_occurrence


if __name__ == "__main__":
    print(occurrence("abbcccdddd"))