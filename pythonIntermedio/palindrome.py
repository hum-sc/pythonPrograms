def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No puede dejar el input vacio, debe ingresar un texto')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    user_input = input('Introduzca una palabra para veriificar si es palindromo: ')
    try:
        print(palindrome(user_input))
    except TypeError:
        print('Solo se puede ingresar texto')


if __name__ == '__main__':
    run()