#Aufgabe2
while True:
    try:
        
        zahl = int(input("Bitte gib eine Zahl ein: "))
        break
    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein.")


if zahl % 3 == 0 and zahl % 4 == 0:
    print("Foobar")
elif zahl % 3 == 0:
    print("Foo")
elif zahl % 4 == 0:
    print("Bar")



input()