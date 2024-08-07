def classique(a, b):
    result=a*a+b*b
    print(result)


def main():
    mainchoice = input('Faites votre choix 1) Classique 2) Réciproque'
                       )
    if mainchoice == '1':
        secondchoice =input('longueur à calculer : 1) hypothénuse 2) coté a 2) coté b')

        if secondchoice == '1':
            cote1 : int= int(input('coté1'))
            cote2: int=int(input('cote2'))
            classique(cote1,cote2)


main()
