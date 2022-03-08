s=input("s=")
sum=0 #to store sum value of roman
temp=0 #to store temporary valur of roman per char or instance
instance=False #boolean value, true if there is instance substraction
i=0
while(i<len(s)):
    instance=False
    if(s[i]=="I"):
        if(i==len(s)-1): #check if char is the last element in string
            temp=1
        elif(s[i+1]=="V"): #check if this char with the next element is intance substraction or not
            temp=4
            instance=True
        elif(s[i+1]=="X"):
            temp=9
            instance=True
        else:
            temp=1
    if(s[i]=="X"):
        if(i==len(s)-1):
            temp=10
        elif(s[i+1]=="L"):
            temp=40
            instance=True
        elif(s[i+1]=="C"):
            temp=90
            instance=True
        else:
            temp=10
    if(s[i]=="C"):
        if(i==len(s)-1):
            temp=100
        elif(s[i+1]=="D"):
            temp=400
            instance=True
        elif(s[i+1]=="M"):
            temp=900
            instance=True
        else:
            temp=100
    if(s[i]=="V"):
        temp=5
    if(s[i]=="L"):
        temp=50
    if(s[i]=="D"):
        temp=500
    if(s[i]=="M"):
        temp=1000
    sum+=temp
    i+=1
    if(instance==True): #skip checking next char if current char and next char is the instance substraction
        i+=1
print(sum)