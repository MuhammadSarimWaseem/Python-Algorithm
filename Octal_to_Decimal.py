# Convert Decimal number to octal using print() output formatting

decimal = int(input("Enter the number:"))
octal = oct(decimal)
print("The octal number of decimal number", decimal, "is:", octal)

#                          OR

decimal = int(input("Enter the number:"))
print('%o' % decimal)
