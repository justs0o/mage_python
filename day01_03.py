import math
list = [2,3,4,5,6,7]
num_list = []
for i in list:

    for num in range(2,int(math.sqrt(i)+1)):
        if num % i ==0 and  num !=i:
            break
        elif num % i != 0 and num ==(int(math.sqrt(i))):
            num_list.append(num)

print (len(num_list))