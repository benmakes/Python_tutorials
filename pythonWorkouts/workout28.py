def join_numbers(numbers):
    """Takes a range of ints as input and returns
    a string of the ints seperated by commas"""

    return ', '.join([str(number) for number in numbers])

print(join_numbers(range(0,10)))