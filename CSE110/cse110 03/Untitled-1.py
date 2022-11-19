#tanveer akerman (RIDHWAN KHAN :v) 
sum1='abcdefg'
sum2='efgabcd'
#sum1=w1+w2
#sum2=w2+w1 result= w1,w2
w1=''
w2=''
for i in range(len(sum1)):
# for  j in sum2:
    j=sum2[0]
    if j ==sum1[i] and (sum1[1] in sum2[:i:1]): #index 4  when we get the e 
        
        w2+=sum1[i:] #index4 sum1[4:] ef
        print(w2)
        w1+=sum1[:i] #sum1[:3]
        print(w1)
        break
    
print(w1,',',w2)
#this code can only run this problem its not a generalized method code