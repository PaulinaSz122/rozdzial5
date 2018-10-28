pula = 30
atrybuty = [["siła", 0], ["zdrowie", 0], ["mądrość", 0], ["zręczność", 0]]
choice = None

while choice != "0":
    print("""
    Witaj w Kreatorze postaci!
    
    0 - koniec
    1 - wyświetl atrybuty
    2 - zmień atrybut
    """)

    choice = input("Wybierasz: ")

    if choice == "0":
        print("Do widzenia!")
    elif choice == "1":
        for item in atrybuty:
            atrybut, wartosc = item
            print(atrybut, "=", wartosc)
    elif choice == "2":
        zmiana = input("Który atrybut chcesz zmienić?: ")
        liczba = 0
        for item in atrybuty:
            atrybut, wartosc = item
            if atrybut == zmiana:
                break
            else:
                liczba += 1

        if liczba < len(atrybuty):
            zmiana_w = int(input("O ile zmienić atrybut? (Aby odjąć, wprowadź liczbę ujemną): "))
            


