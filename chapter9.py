with open('gregor.txt') as f:
    for line in f: 
        print(line, end='')

d1 = {1: 'oak', 2: 'ash', 3: 'lime'}

def write_dic_to_file(d, filename):
    with open(filename, 'w') as f:
        for k, v in d.items():
            print(k, file=f)
            print(v, file=f)

write_dic_to_file(d1, 'c9q2.txt')

def dict_from_file(filename):
    d = {}
    with open(filename) as f:
        while True:
            try:
                k = f.readline()
                v = f.readline().strip
                if k !='' and v !='':
                    d[int(k)] = v
                else:
                    return d
            except ValueError:
                print(f'{k} is not an integer')

def concat_files(file1, file2, file3):
    with open(file3, 'a') as f3, open(file1) as f1, open(file2) as f2:
        print(f1.read(), file=f3, end='')
        print(f2.read(), file=f3, end='')

concat_files('names.txt', 'powers.txt', 'concat.txt')