import random


def generatePassword() :
    upperCase = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    lowerCase = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    symbols = ('!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','<','>',':',';',',','.','?','/','|')
    numbers = ('0','1','2','3','4','5','6','7','8','9')
    
    base = upperCase+lowerCase+symbols+numbers
    password = []
    for i in range(12) :
        char = random.choice(base)
        password.append(char)
    password = ''.join(password)
    return password
def run() :
    password = generatePassword()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()