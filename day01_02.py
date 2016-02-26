list = [1,3,2,3,3,4,2,5,5,7]
list_sorted = sorted(list)
new_list = []
for num in list_sorted:
    if num not in new_list:
        new_list.append(num)
    else:
        continue
print (new_list)