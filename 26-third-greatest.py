def ThirdGreatest(strArr): 
  return sorted([(word, -len(word)) for word in strArr], key=lambda x: x[1])[2][0]
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThirdGreatest(raw_input())  





