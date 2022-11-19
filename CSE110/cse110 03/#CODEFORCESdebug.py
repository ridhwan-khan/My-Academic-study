def new_func():
    #CODEFORCES
    note=int(input())
    listD=[1, 5, 10, 20, 100]
    cnt=0
    x=note
    for i in range(4,-1,-1):
        if x//note[i]==0:
            cnt+=1
        elif x%note[i]!=0: 
            x= note%note[i]
        elif x % note[i] ==0:
            cnt+=1
    print(cnt)

new_func()   