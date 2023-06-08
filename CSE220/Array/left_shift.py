# left shift would cause loss of left values and the right values will get zeros eventually 

N = int(input('Put an integer of how many you want to left shift the array: '))
initial = [1,2,3,4,5]

iter = len(initial) - N

for i in range(iter):
    j = i+N
    initial [i] = initial[j]
    initial [j] = 0 
print(initial)