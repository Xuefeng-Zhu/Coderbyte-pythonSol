def SecondGreatLow(arr): 
  newArr = sorted(set(arr))
  return str(newArr[1]) + " " + str(newArr[-2])
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SecondGreatLow(raw_input())  

