from os import name


def read():
    numbers=[]
    with open('./names.txt','r', encoding='utf-8') as f:
        for line in f:
            numbers.append(line)
    print(numbers)


def read_dict():
    names = {}
    with open('./names.txt','r',encoding='utf-8') as f:
        separator = ':'
        for line in f:
            key, value = line.split(separator)
            names[key.strip()] = value.strip()
    print(names)


def write():
    names = ['Facundo', 'Miguel', 'Pepe']
    with open('./names.txt','w',encoding='utf-8') as f:
        for name in names :
            f.write(name)
            f.write('\n')


def append():
    names = ['Humberto', 'Juana', 'Diana']
    with open('./names.txt', 'a', encoding='utf-8') as f:
        for name in names :
            f.write(name)
            f.write('\n')


def run():
    read_dict()

if __name__ == '__main__':
    run()