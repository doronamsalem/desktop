def minimum_change(amount):
    """return the minimum of change """
    banknotes = [200, 100, 50, 20, 10, 5, 2, 1]
    for i in banknotes:
        if amount // i > 0:
            print(f"{amount // i} of {i}\n")
            amount %= i

minimum_change(214)