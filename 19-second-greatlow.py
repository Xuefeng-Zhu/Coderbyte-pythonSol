# Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers! 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def SecondGreatLow(arr): 
  newArr = sorted(set(arr))
  return "%d %d", %(newArr[1], newArr[-2])
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SecondGreatLow(raw_input())  

