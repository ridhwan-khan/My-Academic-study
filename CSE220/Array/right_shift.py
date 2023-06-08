# N times right shift the array would get N zeros from left 2 time right shift is [0,0,10,20,30]

N = int(input('Input how many times you wanna right shift: '))
initial = [10,20,30,40,50]
iter = len(initial) - N
last = len(initial) -1 

for i in range(iter):
    initial[last] = initial[last - N]
    initial [last - N] = 0
    last -= 1

print(initial)