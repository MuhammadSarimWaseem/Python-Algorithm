# Write a program that prints the percentage marks of high school graduates by taking input
# of sum of their obtained marks and Maximum marks.


maximum_marks = int(input("Enter the maximum marks:"))
obtained_marks = int(input("Enter the obtained marks:"))
percentage = obtained_marks/maximum_marks*100
print("your percentage is: %f" % percentage)
