# Given two integer numbers return their product only if the product
# is equal to or lower than 1000, else return their sum.

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
if number1*number2 <= 1000:
    print(number1*number2)
else:
    print(number1+number2)


# Write a program which take inputs of height and weight from the user and
# output one of the messages underweight,normal and overweight
# underweight=weight < height/2.5
# Overweight=height/2.3 < weight
# normal=height/2.5 <= weight <= height/2.3


weight = float(input("Enter a weight in kilogram:"))
height = float(input("Enter a height in centimeter:"))
if weight < height/2.5:
    print("underweight")
elif height/2.5 <= weight <= height/2.3:
    print("Normal")
elif height/2.3 < weight:
    print("Overweight")
else:
    print("none")


# write a program which takes a string from the user and display the message either it is vowel or constant


s = str(input("Enter a string:"))
if s == ("a" or "e" or "i" or "o" or "u"):
    print("it is vowel")
else:
    print("it is constant")


# take three numbers from user and and print 10 even numbers after the answer


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
total = num1+num2+num3
print(total)
c = []
d = []
if total % 2 == 0:
    for i in range(total, total+20, 2):
        c.append(i)
    print(c)
elif total % 2 != 0:
    for j in range(total+1, total+20, 2):
        d.append(j)
    print(d)
