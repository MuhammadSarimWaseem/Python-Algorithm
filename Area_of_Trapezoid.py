# A quadrilateral with at least one pair of parallel sides is called a trapezoid or trapezium.
# The area K of a trapezoid is given by K = h * (a + b)/2, where a and b are the lengths of
# the parallel sides, h is the height (the perpendicular distance between these sides).

#     Write a program that takes input lengths of two parallel sides and
#       the perpendicular distance between these two parallel lines,
#                and prints the area of this trapezoid.


height = int(input("Enter the height:"))
side_a = int(input("Enter the side a:"))
side_b = int(input("Enter the side b:"))
area_of_trapezoid = height*(side_a+side_b)/2
print("The area of trapezoid is:%f" % area_of_trapezoid)
