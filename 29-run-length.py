def RunLength(strV): 
  mark = 0
  result = ""
  for i in range(1,len(strV)):
    if strV[i-1] != strV[i]:
      result += str(i-mark)+strV[mark]
      mark = i
  return result
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print RunLength(raw_input())  



