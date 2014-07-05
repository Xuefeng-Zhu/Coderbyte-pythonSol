# Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" should return true. 

# Use the Parameter Testing feature in the box below to test your code with different arguments..

def PalindromeTwo(str): 
  str = "".join(i.lower() for i in str if i.isalpha())
  return "true" if str == str[::-1] else "false"
  
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo(raw_input())  
















  