def isPrimo(x) :
    for i in range(1,x+1) :
        if i == 1 or i == x :
            continue
        elif x % i == 0 :
            return False
    return True


def run():
    numero = int(input("Digita un numero: "))
    if isPrimo(numero) :
        print("Es un numero primo")
    else :
        print("No es un numero primo")


if __name__ == '__main__' :
    run()