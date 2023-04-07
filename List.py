# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item, end=",")


# Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
x = reversed(list1)
for item in x:
    print(item, end=",")


# Write a program to accept a string from the user and display characters that are
# present at an even index number.

n = input("Enter word:")
print("oroiginal word:", n)
for i in n[0::2]:
    print(i)

# Iterate the given list of numbers and print only those numbers which are divisible by 5

Given_list = [10, 20, 33, 46, 55]
print("Given list:", Given_list)
for i in Given_list:
    if i % 5 == 0:
        print(i)
#                                 OR
given = (10, 20, 33, 46, 55)
for i in given:
    if i % 5 == 0:
        print(i)

# Write a program to find how many times substring “Emma” appears in the given string.

str_x = ["Emma is good developer. Emma is a writer"]
for i in str_x:
    x = i.count("Emma")
    print("Emma appeared", x, "times")


# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from
# the first list and even numbers from the second list.


return_list = []
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
for i in list1:
    if i % 2 != 0:
        print(i)
        return_list.append(i)
for j in list2:
    if j % 2 == 0:
        print(j)
        return_list.append(j)
print(return_list)

#                                             OR

return_list = []
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
for i in list1:
    if i % 2 != 0:
        return_list.append(i)
for j in list2:
    if j % 2 == 0:
        return_list.append(j)
print(return_list)