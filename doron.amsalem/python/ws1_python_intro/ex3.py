def convert_celsius(temperature):
    """convert celsius temprature to fehrenheit"""
    return int(temperature) * 1.8 + 32

celsius = input("enter temperature in celsius: ")
print(f"the fehrenheit temprature of {celsius}  is {convert_celsius(celsius)}")

