# interview by sara
import time

def every_second(ls):
    """
    :param list:
    :print list element every second:
    """
    while(len(ls) > 0):
        print(ls.pop(0))
        time.sleep(1)


if __name__ == "__main__":
    lis = [1, 2, 3, 4, 5]
    every_second(lis)
