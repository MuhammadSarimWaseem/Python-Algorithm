#  binary searching

list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
n = int(input("enter the number:"))
start = 0
end = len(list)-1
while start <= end:
    midpoint = (start + end)//2
    if list[midpoint] == n:
        print("number found at index", midpoint+1)
        break
    elif list[midpoint] < n:
        start = midpoint + 1
    else:
        end = midpoint - 1
else:
    print("number not found")
