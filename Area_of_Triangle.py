# Area of a triangle can be calculated if lengths of its three sides is known by using the
# Heron’s formula which says that Square root of     [ (s(s−a)(s−b)(s−c)) ]
# where s is half of the perimeter of the triangle that can be calculated by adding length
# of all the three sides and then dividing it by 2.    [  ((a+b+c)/2)   ]

#           (for further information suggested resource is)
#        (https://www.cuemath.com/measurement/area-of-triangle/)


import math

side_a = int(input("Enter the side a:"))
side_b = int(input("Enter the side b:"))
side_c = int(input("Enter the side c:"))
semi_perimeter = (side_a+side_b+side_c)/2
area_of_triangle1 = semi_perimeter * \
    (semi_perimeter-side_a)*(semi_perimeter-side_a)*(semi_perimeter-side_a)
area_of_triangle2 = math.sqrt(area_of_triangle1)
print("The area of triangle is:%f" % area_of_triangle2)
