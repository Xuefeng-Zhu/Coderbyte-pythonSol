def ABCheck(str): 
  return "true" if any(i.find("b")==3 for i in str.split("a")) else "false"
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ABCheck(raw_inut())  
