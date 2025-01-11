def Prime(x,y):
    prime_list = []
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2 ,int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_value = int(input("Enter the first value of range : "))
ending_value = int(input("Enter the last value of range : "))
lst = Prime(starting_value, ending_value)
print(lst)
    
