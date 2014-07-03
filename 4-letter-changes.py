def LetterChanges(str): 
  result = [i if (not i.isalpha()) else (chr(ord(i)+1 if i != 'z' else ord('a'))) for i in str]
  return "".join(i.capitalize() if i in "aeiou" else i for i in result) 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())  



