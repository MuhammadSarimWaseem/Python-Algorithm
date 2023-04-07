# Print First 10 natural numbers using while loop

a = 1
while a <= 10:
    print(a)
    a = a+1


# Write a program to accept a number from a user and calculate the sum of all numbers
# from 1 to a given number

n = int(input("enter the number:"))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)


# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

n = 0
for i in range(9):
    n = n+1
    print("current number:", n, "previous number:", n-1, "sum:", i+n)
