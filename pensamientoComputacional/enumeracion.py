#Este es un ejemplo de la enumeración exhaustiva
def run():
    objetive = int(input('Escoge un entero: '))
    response = 0
    while response**2 < objetive :
        response +=1
    if response**2 != objetive: print('No tiene raíz exacta')
    else : print(f'la raíz es {response}')


if __name__ == '__main__':
    run()