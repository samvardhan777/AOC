with open("Day_1/input.txt", "r") as file:
    lines = file.readlines()

list1 = []
list2 = []
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

sorted_list_1 = sorted(list1)
sorted_list_2 = sorted(list2)

des = [abs(a - b) for a, b in zip(sorted_list_1, sorted_list_2)]

total_distance = sum(des)
print(total_distance)