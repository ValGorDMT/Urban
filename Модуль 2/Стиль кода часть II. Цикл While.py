my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]



new_list =[]
point = 0

while point < len(my_list):
    if my_list[point] < 0:
        break
    elif my_list[point] == 0:
        point += 1
        continue
    else:
        new_list.append(my_list[point])
        print(my_list[point])
        point += 1

print(new_list)

