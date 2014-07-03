def Palindrome(str): 
  str = str.replace(" ", "")
  return "true" if str == str[::-1] else "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print Palindrome(raw_input())  


