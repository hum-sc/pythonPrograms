def divisors(num):
    divisors = []
    try:
        if num < 0 or num == 0 :
            raise ValueError('Debe ingresar un numero positivo o distinto de 0')
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        return ve


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
    except ValueError:
        print('Debes ingresar un numero')


if __name__ == '__main__':
    run()
