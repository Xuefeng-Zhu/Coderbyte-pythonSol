def LetterCount(str): 
  maxC = 0
  maxWord = ""
  for word in str.split():
  	count = 0
    for i in range(len(word)):
      if word[i] in word[i+1:]:
        count += 1 
    if (count > maxC):
    	maxC = count
    	maxWord = word
  if maxC == 0:
  	return -1
  else:
  	return maxWord  
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCount(raw_input())           
