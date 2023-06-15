# Write a Python program to add two matrices.

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
for r in range(3):
    for c in range(4):
        D = A[r][c]+B[r][c]
        print(D, end=" ")
    print("  ")
    
    
# Matrix multiplication


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[3, 4], [5, 6], [7, 8]]
c = [[0, 0], [0, 0], [0, 0]]

for m in range(len(a)):
    for n in range(len(b[0])):
        for k in range(len(b)):
            c[m][n] += a[m][k] * b[k][n]

for row in c:
    print(row)
