def LetterCountI(str): 
  for word in str.split():
    for i in range(len(word)):
      if word[i] in word[i+1:]:
        return word
  return -1  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCountI(raw_input())  
