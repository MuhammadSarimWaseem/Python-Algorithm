#    Write a program that takes input of radius of circle and
#           prints its circumference and area.


import math


radius = int(input("Enter the radius:"))
area = math.pi*radius**2
circumference = 2*math.pi*radius
print("The area of circle is %f" % area)
print("The circumference of circle is %f" % circumference)
