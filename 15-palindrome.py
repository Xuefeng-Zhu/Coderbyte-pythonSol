def PalindromeTwo(str): 
  str = "".join(i.lower() for i in str if i.isalpha())
  return "true" if str == str[::-1] else "false"
  
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo(raw_input())  
















  