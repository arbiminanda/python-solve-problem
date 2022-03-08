n = input("n = ") #ask input for n
arr_string = [] #list for output
temp = "" #variable to store string before added to list
i = 1
while (i <= int(n)):
    temp = ""
    if ((i%3==0) or (i%5==0)):
        if (i%3==0):
            temp += "Kulina"
        if ((i%3==0) and (i%5==0)):
            temp += " x "
        if (i%5==0):
            temp += "Food"
    else:
        temp += str(i)
    arr_string.append(temp) #add string to list
    i += 1
print(arr_string) #print output