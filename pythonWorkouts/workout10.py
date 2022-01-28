def mysum(*items):
    """Sum anything that works with the + operator"""
    if not items:
        #if items is empty we will be out of bounds when we take the 0th index
        print("items evaluated as false")
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum())