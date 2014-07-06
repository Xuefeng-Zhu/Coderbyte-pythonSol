def SimpleMode(arr): 
  Aset = set(arr)
  modeC = 1
  modeN = 0 
  for i in Aset:
    count = arr.count(i)
    if count > modeC:
      modeC = count
      modeN = i
  return modeN if modeC != 1 else -1
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleMode(raw_input())  

