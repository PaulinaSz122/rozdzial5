geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nie znaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących jakiejś osoby.",
        "Keyboard Plaque": "(skojarzone z kamieniem nazębnym) zanieczyszczenia nagromadzone w klawiaturze komputera.",
        "Link Rot": "(obumieranie linków) proces, w wyniku którego linki do stron WWW stają się nieaktualne.",
        "Percussive Maintenance": "(konserwacja perkusyjna) naprawa urządzenia elektronicznego przez stuknięcie.",
        "Uninstalled": "(odinstalowany) zwolniony z pracy; termin szczególnie popularny w okresie bańki internetowej."}

choice = None

while choice != "0":
    print(
    """
    Translator slangu komputerowego
    
    0 - zakończ
    1 - znajdź termin
    2 - dodaj nowy termin
    3 - zmień definicję terminu
    4 - usuń termin
    """
    )

    choice = input("Wybierasz: ")
    print()

    if choice == "0":
        print("Żegnaj.")
    elif choice == "1":
        term = input("Jaki termin mam przetłumaczyć?")
        if term in geek:
            definition = geek[term]
            print("\n", term, "oznacza", definition)
        else:
            print("Niestety, nie znam terminu", term)
    elif choice == "2":
        term = input("Jaki termin mam dodać?: ")
        if term not in geek:
            definition = input("\nPodaj definicję tego terminu: ")
            geek[term] = definition
            print("\nTermin", term, "został dodany.")
        else:
            print("\nTen termin już istnieje! Spróbuj zmienić jego definicję.")
    elif choice == "3":
        term = input("Jaki termin mam przedefiniować?: ")
        if term in geek:
            definition = input("Jaka jest nowa definicja? ")
            geek[term] = definition
            print("\nTermin", term, "został przeterminowany")
        else:
            print("\nTen termin nie istnieje! Spróbuj go dodać.")
    elif choice == "4":
        term = input("Jaki termin mam usunąć?: ")
        if term in geek:
            del geek[term]
            print("\nOK, usunąłem termin", term)
        else:
            print("\nNie mogę tego zrobić! Terminu", term, "nie ma w słowniku")
    else:
        print("\nNiestety,", choice, "to nieprawidłowy wybór.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
