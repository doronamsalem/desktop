def fibunacci(index):
    """
    :param index:
    :return:the value of fibunacci in given index
    """
    prev_ind = 0
    last_ind = 1
    fibu = 0

    if index == prev_ind or index == last_ind:
        return index
    else:
        for x in range(2, index + 1):
            fibu = prev_ind + last_ind
            prev_ind = last_ind
            last_ind = fibu

        return fibu


def fibunacci_recursive(index):
    """
    :param index:
    :return:the value of fibunacci in given index
    """
    if index <= 1:
        return index
    return fibunacci_recursive(index - 1) + fibunacci_recursive(index - 2)


print(fibunacci(7))

print(fibunacci_recursive(7))
