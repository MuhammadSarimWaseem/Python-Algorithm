# Write a program to print multiplication table of a given number

n = int(input("Enter the number:"))
for i in range(1, 11):
    x = n*i
    print(n, "x", i, "=", x)

    #    OR

n = int(input("Enter the number:"))
i = 1
while i < 11:
    x = n*i
    print(n, "x", i, "=", x)
    i = i+1
