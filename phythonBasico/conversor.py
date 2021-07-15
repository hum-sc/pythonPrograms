def convert(option):
    tipoMoneda = ""
    if option == 1 :
        valorDolar = 1.18
        tipoMoneda = "Euros"
    elif option == 2 :
        valorDolar = 19.99
        tipoMoneda = "Pesos Méxicanos"
    else :
        print("Escoja una opcion correcta")
        return 0

    pesos=float(input("¿Cuantos "+tipoMoneda+" tiene? "))
    print("usted tiene "+ str(round(pesos/valorDolar,2)) + tipoMoneda)
    
welcome = "Bienvenido al conversor de monedas a dolares americanos 💰️"
print(welcome)
menu = """

    1 Euros
    2 Pesos Mexicanos

    Ingrese 0 para salir

"""
optionCurrency = 5
while optionCurrency != 0 :
    optionCurrency = int(input(menu + "Ingrese el numero de la moneda que quiere convertir "))
    convert(optionCurrency)
