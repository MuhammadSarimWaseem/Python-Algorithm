# Given two integer numbers return their product only if the product
# is equal to or lower than 1000, else return their sum.

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
if number1*number2 <= 1000:
    print(number1*number2)
else:
    print(number1+number2)
