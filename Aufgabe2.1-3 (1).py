#Aufgabe1

def remove_number_from_list(number_list, number):
    if number in number_list:
        number_list.remove(number)
        print(f"Die Zahl {number} wurde aus der Liste entfernt.")
    else:
        print(f"Die Zahl {number} ist nicht in der Liste enthalten.")

    return number_list


zahlenliste = [1, 2, 3, 4, 5]


zahl = int(input("Bitte gib die Zahl ein, die du aus der Liste entfernen möchtest: "))


aktualisierte_liste = remove_number_from_list(zahlenliste, zahl)
print("Aktualisierte Liste:", aktualisierte_liste)

input()