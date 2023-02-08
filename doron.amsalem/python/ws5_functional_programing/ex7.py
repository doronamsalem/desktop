def make_adder(num1):
    def add_num(num2):
        print(num1 + num2)
    return add_num

add_3 = make_adder(3)
add_3(5)