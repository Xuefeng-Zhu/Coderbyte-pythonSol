def StringScramble(str1,str2): 
  list1 = list(str1)
  for i in str2:
    try:
      list1.remove(i)
    except:
      return "false"
  return "true"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble(raw_input())  




