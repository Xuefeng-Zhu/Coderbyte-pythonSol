def NumberAddition(str): 
  mark = 0 
  result = 0 
  for i in range(1,len(str)+1):
    if not str[mark:i].isdigit():
      if (mark+1 != i):       
        result += int(str[mark:i-1])
      mark = i
  if str[mark:i].isdigit():
    result += int(str[mark:])
  return result
        
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print NumberAddition(raw_input())           
