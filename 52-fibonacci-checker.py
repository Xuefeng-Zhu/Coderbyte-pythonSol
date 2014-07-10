def FibonacciChecker(num): 
  fList = [0, 1]
  while fList[-1] < num:
    fList.append(fList[-2]+fList[-1])
  return "yes" if fList[-1]==num else "no"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FibonacciChecker(raw_input())           
