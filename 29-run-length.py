def RunLength(str): 
  mark = 0
  result = ""
  for i in range(1,len(str)+1):
    if i==len(str) or str[i-1] != str[i]:
      result += "%d%s" %(i-mark,str[mark])
      mark = i
  return result
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print RunLength(raw_input())           
