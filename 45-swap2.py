def SwapII(str): 
  result = [i.lower() if i.isupper() else i.upper() for i in str]
  first = -1
  for i in range(len(result)):
    if result[i].isdigit():
      if first == -1:
        first = i
      else:
        result[first], result[i] = result[i], result[first]
        first = -1
  return "".join(result) 
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SwapII(raw_input()) 