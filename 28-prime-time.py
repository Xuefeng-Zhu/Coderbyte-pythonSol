import math
def PrimeTime(num): 
  if num % 2 == 0:
    return "false"
  for i in range(3, int(math.sqrt(num)), 2):
    if num % i == 0:
      return "false"
  return "true"

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeTime(raw_input())  






