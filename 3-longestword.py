# def LongestWord(sen): 
#   return max((len(word),word) for word in sen.split() if word.isalpha())[1]
    
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print LongestWord(raw_input())           
def LongestWord(sen): 
   max = (0,"")
   for i in [(len(word),word) for word in sen.split() if word.isalpha()]:
     if (i[0] > max[0]):
        max = i
   return max[1]
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           

