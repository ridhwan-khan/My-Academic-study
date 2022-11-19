#RIDHWAN KHAN 22301143
given = {99:(2,'avb34Af9'), 101:(9,'g4hfD6hh'), 67:(8,'99oikjF3')}
result={}
for key,values in given.items():
    print(key,values)
    number=0
    characters=0
    num_count=0
    count=0
    for i in values[1]:
        if ord("0")<=ord(i)<=ord("9"):
            number+= int(i)*count
            num_count+=1
            count+=1
        else:
            
            characters+=ord(i)*count
            count+=1
            
    new_key = (characters +number)% (key+values[0])
    result[new_key]=(values[1],num_count)
print(result)