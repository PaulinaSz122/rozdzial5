inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]
print("Elementy twojego inwentarza:")
for item in inventory:
    print(item)

print("Twój dobytek zawiera", len(inventory), "elementy(-ów).")
input("\nAby kontynuować grę, naciśnij klawisz Enter.")

if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

index = int(input("\nWprowadź indeks elementu inwentarza: "))

print("Pod indeksem", index, "znajduje się", inventory[index])

start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
finish = int(input("Wprowadź indeks wyznaczający koniec wycinku: "))

print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

chest = ["złoto", "klejnoty"]

print("Znajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

print("Wymieniasz swój miecz na kuszę.")

inventory[0] = "kusza"

print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

print("Zużywasz swoje złoto i klejnoty na zakup kuli do wróżenia.")

inventory[4:6] = ["kula do wróżenia"]

print("Twój aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

print("Twoja kusza i zbroja zostały skradzione przez złodziei.")
del inventory[:2]

print("Twój aktualny inwentarz to:")
print(inventory)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
