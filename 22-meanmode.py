def MeanMode(arr): 
  avg = sum(arr) / len(arr)
  mode = 0
  for i in set(arr):
    if arr.count(i) > arr.count(mode):
      mode = i
  return 1 if avg == mode else 0
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MeanMode(raw_input())  

