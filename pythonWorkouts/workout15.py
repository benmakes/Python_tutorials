def get_rainfall():
    """Produces a rainfall report from multiple inputs from the user"""
    rainfall = {}
    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break
        try:
            mm_rain = int(input('Enter mm rain: '))
        except ValueError:
            print('You didn\'t enter a valid integer. Try again.')
            continue
        
        rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

get_rainfall()