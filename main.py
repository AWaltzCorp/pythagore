
from math import *
import function as f


def main():
    mainchoice = input('Faites votre choix 1) Classique 2) Réciproque: ')

    if mainchoice == '2':
        cote1 = int(input('côté1: '))
        cote2 = int(input('côté2: '))
        hypothenuse = int(input('hypothénuse: '))
        result = f.reciproque(cote1, cote2)
        if result == (hypothenuse * hypothenuse):
            print('Le triangle ABC est rectangle')
        else:
            print('Le triangle ABC n\'est pas rectangle')

    elif mainchoice == '1':
        secondchoice = input('Longueur à calculer : 1) hypothénuse 2) autre côté: ')

        if secondchoice == '2':
            hypothenuse = int(input('hypothénuse: '))
            cote2 = int(input('côté: '))
            print(f'Longueur du côté calculée : {f.classique2(hypothenuse, cote2)}')

        elif secondchoice == '1':
            cote1 = int(input('côté1: '))
            cote2 = int(input('côté2: '))
            print(f'Hypothénuse calculée : {f.classique(cote1, cote2)}')


main()
