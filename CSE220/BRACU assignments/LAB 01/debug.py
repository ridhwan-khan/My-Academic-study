# #problem 2 

# import numpy as np 
# def discardCards(cards,number):
#   ####*******FOR TASK 2, PLEASE RETURN THE array after converting it into the numpy array first, We will discuss the details..
#   ### ON THE NEXT CLASS
#   ## example of how to make a numpy array
#   ## lets say your answer is stored inside the array : arr=[1,2,3,4,5]
#   ## while returning, please use the statement : return np.array(arr)
#   ##also dont forget to run the top code cell block to import numpy***
#   # TO DO
#     remove_element = number
#     cards = np.array(cards, dtype= object)
    
#     count = 0   #//TODO: i doubt if i need to return as its a pass by reference let's see 
#     print(len(cards))
#     # for iter in range (len(cards)):
#     iter = 0
#     while remove_element in cards:


#         if cards[iter] == remove_element:
#             count += 1 
#             iter += 1
#             print('if check')
#         else:
#             if count > 0: 
#         #we need to shring so left shift korbo count times
#                 head = iter - count
#                 start_from = head
#                 tail = iter
#                 for k in range (head, len(cards)):
#                     cards[head] = cards[tail] 
#                     cards[tail] = None
#                     tail += 1
#                     head += 1
#                     print(cards) 
#                     print(tail)
#                 count = 0
#                 iter = start_from #As i ve shifted n times and now again checking je ache kina pasapasi n elements
#                 # tail = iter
#             else: 
#                 print("continue")
#                 iter += 1 
#                 continue
#         print(f"i = {iter} cards: {cards}")
#     return cards


# print("///  Test 02: Discard Cards  ///")
# cards = np.array([1,2,2,2,8,2,2,5,7])
# returned_value = discardCards(cards, 2)
# print(f'Task 2: {returned_value}') # This should print [1, 3, 8, 5, 7, None, None, None, None]
# # unittest.output_test(returned_value, [1, 3, 8, 5, 7, None, None, None, None])

# #TODO fix the iter thing karon oikhane to left shift hoye 2 samne ese porse ei logic khatbe na 
