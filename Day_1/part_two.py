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

print(type(sorted_list_1))
dict_1 = {}

for i in  sorted_list_1:
    keys = i
    count=0
    for i in sorted_list_2:
        if keys == i:
            count=count+1
    dict_1[keys] = count



final_res=0
for k,v in dict_1.items(): 
    result = k*v
    final_res=final_res+result

print(final_res)
