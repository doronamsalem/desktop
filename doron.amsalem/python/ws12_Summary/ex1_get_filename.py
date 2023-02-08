# review by vica
import os

def file_name(path):
    """:param path: of file\n:return: name of the file"""
    try:
        if not os.path.exists(path):
            raise OSError
        return os.path.basename(path)

    except TypeError:
        raise TypeError("path must be string")

    except OSError:
        raise OSError("path doesn`t exist")


if __name__ == '__main__':
    print(file_name("a"))

