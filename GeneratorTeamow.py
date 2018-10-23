import random

koszyczek = ['a','b','c','d','e','f','g','h','i','j']
team1= []

pojemnoscKoszyczka = len(koszyczek)

polowa = pojemnoscKoszyczka//2

for liczba in range(polowa):
    losowyElement = random.choice(koszyczek)
    team1.append(losowyElement)
    koszyczek.remove(losowyElement)
print("Team 1:", team1)
print("Team 2:", koszyczek)