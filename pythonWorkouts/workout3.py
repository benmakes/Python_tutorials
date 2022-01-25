def run_timing():
    runs = 0
    tot_time = 0.0
    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break
        try:
            tot_time += float(one_run)
            runs += 1
        except ValueError:
            print('That\'s not a number!')
    
    print(f'Average of {tot_time/runs:.2f}, over {runs} runs')

run_timing()
