#decimal to binary #ungraded 26 lab 02 
start=int(input('input'))
store=start
x=0
bin=[ ]
while store%2>=0:
    
    bin.append(store%2)
    
    store=store//2
    print(store,end=' ')
    print()
    if store==0:
        break

print(bin,end=' ')
print()
for z in bin[-1::-1]:
    print(z,end='')
