#pascal traignle RIDHWAN KHAN
row=(int(input()))
list1=[]
for i in range (row):
    temp_list=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp_list.append(int(1))
        else:
            temp_list.append(list1[i-1][j-1]+list1[i-1][j])    #              1
    list1.append(temp_list)                                            
print(list1)

for i in range (len(list1)):
    la=list1[i]
    for j in range(len(la)):
        print(la[j],end=" ")
    print()
