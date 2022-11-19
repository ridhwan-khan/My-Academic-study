def function_name(list1):
    list2=[]
    for x in list1:
        if x not in list2:
            list2.append(x)
        elif x in list2 and list2.count(x)<2:
            list2.append(x)
    removed=len(list1)-len(list2)
    print('Removed',removed)
    
    # print(list2) 

print(function_name([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))