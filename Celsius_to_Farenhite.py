# Write a program for temprature conversion by taking input from the user
# (celsius to farenhite or farenhite to celsius)

conversion = input("celsius to farenhite or farenhite to celsius:")
if conversion == "celsius to farenhite":
    celsius = int(input("Enter a celsius:"))
    farenhite = celsius+32*(9/5)
    print("farenhite", farenhite)
elif conversion == "farenhite to celsius":
    farenhite = int(input("Enter a farenhite:"))
    celsius = farenhite-32*(5/9)
    print("celsius"+celsius)
else:
    print("none")
