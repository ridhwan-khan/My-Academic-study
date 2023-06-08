#procedure 1
initial = [1,2,3,4,5]
i = 0 
j = len(initial) - 1
while i< j :
    temp = initial[j]
    initial[j] = initial [i]
    initial[i] = temp
    i+=1
    j -=1 

print(initial)

#procedure 2
initial = [1,2,3,4,5]
j = len(initial)-1
iter = len(initial) // 2
for i in range(iter):
    temp = initial[j]
    initial[j] = initial[i]
    initial [i] = temp
    j -= 1

print(initial)

