def ArithGeoII(arr): 
  result = "Arithmetic"
  for i in range(1,len(arr)-1):
    if arr[i+1] - arr[i] != arr[1] - arr[0]:
      result = "Geometric"
      for i in range(1, len(arr)-1):
        if arr[i+1] / arr[i] != arr[1] / arr[0]:
          result = -1
      break
  return result
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeoII(raw_input())           
