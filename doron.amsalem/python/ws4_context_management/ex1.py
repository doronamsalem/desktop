def print_text_capital(path):
    """
    param path to a file:
    :return content of file in capital letters:
    """
    with open(path, "r") as make_capital:
        print(make_capital.read().upper())


def without_context_managers(path):
    try:
        f = open(path, "r")
        print(f.read().upper())
    finally:
        f.close()


print_text_capital("/Users/doronamsalem/Desktop/aa.py")
without_context_managers("/Users/doronamsalem/Desktop/aa.py")
