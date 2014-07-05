def Division(num1,num2): 
  while num2 != 0:
    num1, num2 = num2, num1%num2 
  return num1  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print Division(raw_input())           
