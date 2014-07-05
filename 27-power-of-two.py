import math
def PowersofTwo(num): 
  temp = math.log(num,2)
  return "true" if temp == math.floor(temp) else "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PowersofTwo(raw_input())           
