import random

koszyczek = ['a','b','c','d','e','f','g','h','i','j']


def generuTeamy(lista):
    random.shuffle(lista)
    polowa = len(lista)//2
    team1 = lista[0:polowa]
    team2 = lista[polowa:]
    return team1,team2

print (generuTeamy([1,2,3,4,5,6,7,8,9,0]))
