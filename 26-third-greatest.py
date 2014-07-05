def ThirdGreatest(strArr): 
  dStr = {}
  for word in strArr:
    dStr[len(word)] = dStr.get(len(word),[]) + [word]
  temp = sorted(len(word) for word in strArr)
  return dStr[temp[-3]][-1]
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThirdGreatest(raw_input())  
















  