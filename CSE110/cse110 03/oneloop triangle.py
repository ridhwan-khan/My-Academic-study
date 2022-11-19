r1=int(input())
for i in range (1,r1+1):
    print(i,'check')
                                         # print(' ')
    if  i==1  or  i==2 or i==r1:
        # print('check1')
        print('s'*(r1-i)+'*'*i)
    else:
                                     #bal ekhane ami column i nilam na bolod ridhwan -_- 
                                        # if i==r1:
                                        #     print('*')
                                        # elif i ==r1+1:
                                        #     print('*')
                                        # else:
                                        #     print(' ')
        print('s'*(r1-i)+'*'+'s'*(i-2)+'*')
    