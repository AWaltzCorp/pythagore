from math import *
import function
import web_pdb;

web_pdb.set_trace()


def main():
    mainchoice = input('Faites votre choix 1) Classique 2) Réciproque'
                       )
    if mainchoice == '2':
        cote1: int = int(input('coté1'))
        cote2: int = int(input('cote2'))
        hypothenuse: int = int(input('hypothénuse'))
        result = function.reciproque(cote1, cote2)
        if result ==(hypothenuse * hypothenuse):
            print('Le triangle ABC est rectangle')
        if result != (hypothenuse * hypothenuse):
            print('Le triangle ABC n est pas rectangle')

    if mainchoice == '1':
        secondchoice = input('longueur à calculer : 1) hypothénuse 2) coté autre')
        if secondchoice == '2':
            hypothenuse: int = int(input('hypothénuse'))
            cote2: int = int(input('cote2'))
            function.classique2(hypothenuse, cote2)

        if secondchoice == '1':
            cote1: int = int(input('coté1'))
            cote2: int = int(input('cote2'))
            function.classique(cote1, cote2)


main()
