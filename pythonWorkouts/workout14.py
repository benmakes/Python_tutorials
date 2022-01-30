MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
    """Prompts user to order another item from the menu. If 
    the order is not on the menu the user is scolded. If an empty
    string is entered the total price is tabulated."""

    order = ''
    total = 0

    while True:
        order = input('Order: ').strip()

        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price}. The total is {total}.')

        else:
            print(f'{order} is not on the menu today.')
    
    print(f'Your total is {total}.')

restaurant()