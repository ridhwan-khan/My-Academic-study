# You must run this cell to install dependency

import fhm_unittest as unittest
import numpy as np

# Test 01: Play Right
def playRight(sequence,beats):
    for i in range(len(beats)):
        if beats[i] == 1:   
            x = len(sequence) - 1
            last_shift_element = sequence[x]  
            for iter in range(x):
                
                sequence[x] = sequence[x-1]
                x -= 1
            sequence[x] = last_shift_element
        continue
    return sequence

print("///  Test 01: Play Right  ///")
sequence=np.array([10,20,30,40,50,60])
beats = np.array([1,0,0,1,0,1])
returned_value = playRight(sequence, beats) 
print(f'Task 1: {returned_value}') # This should print [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, np.array([40, 50, 60, 10, 20, 30]))