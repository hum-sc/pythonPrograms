def divisors(num):
    divisors = []
    try:
        assert num>0, 'Debe ingresar un numero mayor que 0'
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except AssertionError as ae:
        return ae


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
    except ValueError:
        print('Debes ingresar un numero')


if __name__ == '__main__':
    run()
