string1=input('input')
low=''
up=''
dig=''
sChr=''
new=''
mod=''
for i in string1:
    if i!=' ':
        mod+=i
print(mod)
for i in mod:
    if 67<=ord(i)<=97:
        up+=i
    elif 97<=ord(i)<=122:
        low+=i
    elif ord('1')<=ord(i)<=ord('9'):
        dig+=i
    else:
        sChr+=i
# print('Lower-case',low)
# print("Upper-case",up)
# print('Special-character',sChr)
# print('digits',dig)
for i in range(len(low)):
    new+=up[i]+low[i]+dig[i]+sChr[i]
print('Lower-case',low)
print("Upper-case",up)
print('Special-character',sChr)
print('digits',dig)
print('New',new)    