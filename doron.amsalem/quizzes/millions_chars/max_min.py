# interview by sara
def max_min_dictionary(dictionary):
    """
    :param dictionary: of characters and numbers
    :return: max key and his number of occurrence as variables
            and min key and his number of occurrence as variables
    """
    # make a list of all dictionary keys and values
    dict_vals = list(dictionary.values())
    dict_keys = list(dictionary.keys())
    # find the index of minimum and maximum values
    max_ind = dict_vals.index(max(dict_vals))
    min_ind = dict_vals.index(min(dict_vals))
    # print the mach keys of the min max values
    return dict_keys[max_ind], max(dict_vals), dict_keys[min_ind], min(dict_vals)


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3}
    maximum, max_occurre, minimum, min_occurre = max_min_dictionary(d)
    print("max value's key:{} appeared {}\nmin value's key:{} appeared {}".format(
        maximum, max_occurre, minimum, min_occurre))
