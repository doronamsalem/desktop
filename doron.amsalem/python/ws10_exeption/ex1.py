#code review by sahar
def div(a, b):
    """
    :param a, b: two numbers
    :return: division of the numbers
    """
    try:
        return a / b

    except TypeError:
        print("the parameters aren`t valid numbers")
        raise TypeError

    except ZeroDivisionError:
        print("tried to divide by zero")
        return None


        print(div("d", 0))

