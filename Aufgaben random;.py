
#Aufgabe1
min = float(input("Gebe Zeit in Minuten an: "))

stunden = int(minutes // 60)
min %= 60
sec = round((minutes % 1) * 60)


output = f"{stunden}h {min}m {sec}sec"



print(output)

#--------------------------------------------------------

#Aufgabe2

import random


geheime_zahl = random.randint(1, 100)

while True:
    try:
    
        eingabe = input("Rate die geheime Zahl (1-100): ")

        if not eingabe.isdigit():
            print("Bitte gib eine gültige Zahl ein.")
            continue

        geratene_zahl = int(eingabe)

        if geratene_zahl < geheime_zahl:
            print("Die gesuchte Zahl ist größer.")
        elif geratene_zahl > geheime_zahl:
            print("Die gesuchte Zahl ist kleiner.")
        else:
            print(f"Glückwunsch! Du hast die geheime Zahl {geheime_zahl} erraten.")
            break

    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")
        #----------------------------------------------------

        #Aufgabe3

        
eingabe = input("Gib einen beliebigen Text ein: ")


summe_zahlen = 0
bereinigter_text = ""


for char in eingabe:
    
    if char.isnumeric():
        summe_zahlen += int(char)
    else:
        bereinigter_text += char

print(f"Die Summe der Zahlen im Text beträgt: {summe_zahlen}")
print(f"Der bereinigte Text ohne Zahlen lautet: {bereinigter_text}")