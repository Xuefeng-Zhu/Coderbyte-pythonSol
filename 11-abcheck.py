# Have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.
def ABCheck(str): 
  return "true" if any(i.find("b")==3 for i in str.split("a")) else "false"
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ABCheck(raw_inut())  
