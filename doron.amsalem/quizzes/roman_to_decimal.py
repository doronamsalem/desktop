def roman_to_decimal(roman_num):
    decimal = [0]
    for roman_digit in roman_num:
        # I = 1
        if roman_digit == 'I':
            decimal.append(1)
        # V = 5, IV = 4
        elif roman_digit == 'V':
            if decimal[len(decimal) - 1] < 5:   # IV -> 1,5 = 4
                decimal.append(3)
            else:
                decimal.append(5)
        # X = 5, IX = 4
        elif roman_digit == 'X':
            if decimal[len(decimal) - 1] < 10:   # IV -> 1,10 = 9
                decimal.append(8)
            else:
                decimal.append(10)
        # L = 50
        elif roman_digit == 'L':
            decimal.append(50)
        # C = 100
        elif roman_digit == 'C':
            decimal.append(100)
        # D = 500
        elif roman_digit == 'D':
            decimal.append(500)
        # M = 1000
        elif roman_digit == 'M':
            decimal.append(1000)

    return sum(decimal)


if __name__ == "__main__":

    print(roman_to_decimal("XIXI"))
