# digit1={99:(2,'avb34Af9'),101:(9,'g4hD6hh'),67:(8,'99oikjF3')}

# result_dict={} #consist of a string and a random number
# digitStore=[]

# for values in digit1.values():
#     # print(values) #[all the tuples]
#     for string_values in  range(len(values[1])):
#         # print( values[1][string_values],'string value:',string_values ,end=' ')
#         if ord('1')<= ord(values[1][string_values])<ord('9'):
#             digitStore+=(int(values[1][string_values])*(string_values))
#             # print(values[1][string_values] )
#             # print( str(string_values))
# print(digitStore)
                
            

#     # print(digitStore)       

#COLLECTED FROM BRACU GC

n = {99:(2,'avb34Af9'), 101:(9,'g4hfD6hh'), 67:(8,'99oikjF3')}
dictionary={}
# count=0
for i in n:
    count=0
    alphabet=0
    numerical=0
    x,y=n[i]
    for j in range(len(y)):
        helo = y[j]
        if ord("0")<=ord(helo)<=ord("9"):
            numerical+=int(helo)*j
            count+=1
        else:
            alphabet+=ord(helo)*j
    sum1=(alphabet+numerical)%(i+x)
    dictionary[sum1]=(y,count)
print(dictionary)