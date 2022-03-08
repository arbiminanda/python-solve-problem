s = input("s = ")
t = input("t = ")
occ_s = 0 #to store the occurence of spesific char in string s
occ_t = 0 #to store the occurence of spesific char in string t
simplified_s = "".join(set(s)) #to get just unique char from string s
for i in simplified_s:
    occ_s = s.count(i)
    occ_t = t.count(i)
    t = t.replace(i, "") #remove char in string t that occur in string s
    if (occ_t > occ_s):
        for j in range(occ_t - occ_s):
            t += i #add removed char if the occurence of char in string t is more than string s
print(t) #print the output