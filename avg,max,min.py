# take input of marks and print the average,maximum and minimum marks

marks = float(input("Enter marks:"))
maximum = 0
minimum = 100
n = 0
total = 0
while marks >= 0:
    if marks >= maximum:
        maximum = marks
    if marks <= minimum:
        minimum = marks
    n = n+1
    total = total+marks
    average = total/n
    marks = float(input("Enter marks:"))
print(f"average:{average}")
print(f" maximum:{maximum}")
print(f" minimum:{minimum}")
