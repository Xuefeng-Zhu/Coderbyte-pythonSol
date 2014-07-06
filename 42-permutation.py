
# def swap(nList,i):
#   nList[i],nList[i-1] = nList[i-1], nList[i]
#   for x in range(i, -1):
#     if int(nList[i]) > int(nList[i+1]):
#       nList[i],nList[i+1] = nList[i+1], nList[i]

# def PermutationStep(num): 
#   nList = list(str(num))
#   for i in range(-1, -len(nList), -1):
#     if int(nList[i]) > int(nList[i-1]):
#       swap(nList,i)
#       return "".join(nList)
#   return -1
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print PermutationStep(raw_input())  

# Using the Python language, have the function PermutationStep(num) take the num parameter being passed and return the next number greater than num using the same digits. For example: if num is 123 return 132, if it's 12453 return 12534. If a number has no greater permutations, return -1 (ie. 999). 

# Use the Parameter Testing feature in the box below to test your code with different arguments.
def PermutationStep(num): 
  temp = str(num)
  for i in range(len(temp)-1, 0, -1):
    if temp[i] > temp[i-1]:
      return temp[:i-1] + temp[i] + "".join(sorted(temp[i-1]+temp[i+1:]))
  return -1 
        
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PermutationStep(raw_input())           

















  















#   