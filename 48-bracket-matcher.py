def BracketMatcher(str): 
  temp = []
  for i in str:
    if i == "(":
      temp.append(temp)
    elif i == ")":
      try:
        temp.pop()
      except:
        return 0
  return 0 if len(temp) else 1  
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print BracketMatcher(raw_input()) 