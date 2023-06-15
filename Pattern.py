# Write a program to print the following number pattern using a loop.

for i in range(6, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\t")
    
    