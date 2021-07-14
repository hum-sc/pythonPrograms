##Usaremos funciones anonimas
def run() :
    palindromo = lambda string : string==string[::-1]
    print(palindromo('holoh'))


if __name__ == '__main__':
    run()