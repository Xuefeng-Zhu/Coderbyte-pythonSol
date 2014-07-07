def DashInsertII(num): 
  result = ""
  for i in str(num):
    if (len(result)==0):
      result += i 
      continue
    if int(i)%2 == 1 and int(result[-1])%2==1:
      result += "-" + i
    elif int(i) != 0 and int(i)%2 == 0 and int(result[-1]) != 0 and int(result[-1])%2 == 0:
      result += "*" + i
    else:                
      result += i
  return result 
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print DashInsertII(raw_input())           
