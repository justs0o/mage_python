number = 10
count = 0
while count <3:
    print_number = int(input("Please input your number: "))
    if number == print_number:
        print ("congratulations！ you win!")
        break
    elif number > print_number:
        print("smaller")
        count +=1
    else:
        print ("big")
        count +=1
else:
    print ("Oops! you fail!")
