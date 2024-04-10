
print("Gebe eine Nummer ein:")


while True:
    try:
       
        number = int(input())
        break 
    except ValueError:
       
        print("That is not a valid number. Please try again.")
        
if number % 3 == 0 and number % 4 == 0:
    print("Foobar")
elif number % 3 == 0:
    print("Foo")
elif number % 4 == 0:
    print("Bar")
else:
    print("The number is not divisible by 3 or 4.")