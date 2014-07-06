def CaesarCipher(str,num): 
  return "".join(chr(ord(i)+num) if i.isalpha() else i for i in str)
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print CaesarCipher(raw_input())           
