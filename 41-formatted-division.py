def FormattedDivision(num1,num2): 
  temp =  "%.4f" %(float(num1)/num2)
  return "{:,}".format(float(temp))
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FormattedDivision(raw_input())  
















  