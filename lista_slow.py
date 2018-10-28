import random

lista = ["Python", "Pies", "Kot", "Robot", "Człowiek", "Programowanie"]

while len(lista) != 0:
    slowo = random.choice(lista)
    print(slowo)
    lista.remove(slowo)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
