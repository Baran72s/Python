#Aufgabe2
def remove_duplicates_from_list(number_list):
    unique_numbers = []
    duplicates = []

    for number in number_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
        else:
            duplicates.append(number)

    for duplicate in duplicates:
        while duplicate in number_list:
            number_list.remove(duplicate)

    return number_list


zahlenliste = [1, 2, 3, 4, 2, 5, 3]


bereinigte_liste = remove_duplicates_from_list(zahlenliste)
print("Bereinigte Liste:", bereinigte_liste)

input()