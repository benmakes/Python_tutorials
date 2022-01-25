def hex_output():
    """Asks the user to input a hexidecimal number and converts it to decimal format"""
    decnum = 0
    hexnum = input('Enter a hexidecimal number: ')

    try:
        for power, one_digit in enumerate(reversed(hexnum)):
            decnum += int(one_digit, 16) * (16 ** power)
        print(decnum)
    except ValueError:
        print('You did not enter a number in hexidecimal format')

hex_output()