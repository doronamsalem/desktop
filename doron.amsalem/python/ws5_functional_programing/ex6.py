def is_name(*args, **kwargs):
    for key, item in kwargs.items():
        if key == "name":
            print(item)

is_name(6, 7, name="aaa", my="bbb")