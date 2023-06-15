# selection sorting

x = [20, 10, 40, 66, 90, 11, 67, 58, 99]
for i in range(0, len(x)):
    for j in range(i+1, len(x)):
        if x[i] > x[j]:
            c = x[i]
            x[i] = x[j]
            x[j] = c
    print(x[i])
