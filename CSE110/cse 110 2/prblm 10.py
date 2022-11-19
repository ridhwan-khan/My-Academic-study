num= int(input('enter a number '))
dig=0 

while num != 0 : 
    dig =num%10 
    num=num//10 
    print(dig, end =' ' )
