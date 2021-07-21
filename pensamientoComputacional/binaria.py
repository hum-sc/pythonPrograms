def run():
    objetivo = int(input('Introduce un numero: '))
    li = 0
    ls = max(1.0, objetivo)
    epsilon = 0.000000000000001
    mid = (ls+li)/2
    while abs(mid**2 - objetivo) >= epsilon:
        if mid**2 < objetivo:
            li = mid
        else:
            ls = mid
        mid = (ls+li)/2
    print(f'La raiz cuadrada de {objetivo} es {mid}')


if __name__ == '__main__':
    run()