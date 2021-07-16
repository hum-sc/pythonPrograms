import os
import platform
import random
import time

IMÁGENES_AHORCADO = ['''
  +---+
  |   |
      |
      |
      |
      |
 =========''', '''
    +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
    +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
    +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
    +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
    +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
    +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']


def get_data():
    words = []
    with open('./data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            #Quitamos espacion, acentos y hacemos full máyusculas
            new_sentence = line.maketrans('áéíóú', 'aeiou')
            line = line.translate(new_sentence)
            words.append(line.strip().upper())
    return words


def get_scores():
    scores = {}
    separator = ':'
    with open('./scores.txt','r',encoding='utf-8') as f:
        for line in f:
            key, value = line.split(separator)
            print(key,' : ',value)


def save_scores(score):
    name = input('Ingrese su nickname: ')
    with open('./scores.txt', 'a', encoding='utf-8') as f:
        f.write(name+':'+str(score))
        f.write('\n')


def get_clear():
    system = platform.system()
    if system == 'Windows' : return 'cls'
    return 'clear'


clr = get_clear()


def game():
    #Escogemos una palabra y creamos el underline y la lista
    words = get_data()
    chosen_word = random.choice(words)
    word_list = [letter for letter in chosen_word]
    underscored_word = ['_'] * len(chosen_word)
    indexed_letters = {}
    #Dibujando la orca

    #Variable de la vida y puntaje
    live = 0
    score_word = len(chosen_word)*0.75
    #Indexamos las letras
    for indx, letter in enumerate(chosen_word):
        if not indexed_letters.get(letter):
            indexed_letters[letter] = []
        indexed_letters[letter].append(indx)
    #El juego
    while live<6:
        os.system(clr)
        print(IMÁGENES_AHORCADO[live])
        print('Adivina la palabra')
        #Imprimimos las coincidencias de la palabra
        for element in underscored_word:
            print(element, ' ', end='')
        print('\n')
        #Leemos la letra a ingresar
        letter = input('Ingresa una letra: ').strip().upper()
        try:
            if letter.isalpha() and len(letter) == 1:
                if letter in word_list and not letter in underscored_word:
                    for indx in indexed_letters[letter]:
                        underscored_word[indx] = letter
                else :
                    live+=1
                if not '_' in underscored_word:
                    os.system(clr)
                    print('Haz adivinado la palabra: ', chosen_word)
                    break
            else: raise ValueError('Debes ingresar solamente una letra')
        except ValueError as ve:
            os.system(clr)
            print(ve)
            time.sleep(1)
            
    if live==6:
        os.system(clr)
        print(IMÁGENES_AHORCADO[6])
        print('Lo siento, la palabra era: ',chosen_word)
        return 0
    else: return score_word


def run():
    home = """
    Bienvenido al juego del ahorcado 🏁️
    by Humberto SC

    Presiona 1 para comenzar a jugar 🎮️
    Presiona 2 para ver el scoreboard 🌐️
    Cualquier otra tecla para salir
    """
    os.system(clr)
    print(home)
    state = 0

    try : state = int(input('     '))
    except ValueError : os.system(clr)
    
    score = 0
    while state == 1:
        score+=game()
        save = 0
        print('Tu puntaje es: ', score)
        try :
            state = int(input('Introduce 1 para jugar de nuevo\nIntroduce cualquier otra tecla para salir\n'))
        except: 
            state = 0
        if state == 0:
            os.system(clr)
            print('Tu puntaje fue:', score,""" ¿Deseas guardarlo?
            1 - Sí
            2 - No
            """)
            try:
                save=int(input(    ))
                if save != 1 and save != 2 : raise ValueError('Debes ingresar 1 o 2')
            except ValueError: print('Debes ingresar 1 o 2')
            if save == 1:
                save_scores(score)
            else: os.system(clr)
    if state == 2:
        os.system(clr)
        print('Scoreboard')
        get_scores()


if __name__ == '__main__':
    run()