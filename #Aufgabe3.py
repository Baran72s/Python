#Aufgabe3
def print_tree(width, height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2*i - 1)
        print(spaces + stars)


width = int(input("Bitte gib die Breite des Baumes ein: "))
height = int(input("Bitte gib die Höhe des Baumes ein: "))

print_tree(width, height)