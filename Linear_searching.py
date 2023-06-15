# linear searching/ linear sequence search

my_list = [44, 74, 24, 94, 14, 54, 84]
target_number = 848
for i in range(len(my_list)):
    if my_list[i] == target_number:
        print(f"Target {target_number} found at index {i}")
    elif target_number not in my_list:
        print(f"Target {target_number} not found in the list.")
        break
