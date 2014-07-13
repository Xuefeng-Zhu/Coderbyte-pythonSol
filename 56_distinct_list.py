def DistinctList(arr): 
  a_set = set(arr)
  result = 0 
  for num in a_set:
    result += arr.count(num) - 1
  return result
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print DistinctList(raw_input())  
















  