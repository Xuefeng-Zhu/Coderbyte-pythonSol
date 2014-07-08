import math
def NumberSearch(str): 
  return int(round(float(sum(int(i) for i in str if i.isdigit()))/len([i for i in str if i.isalpha()])))
  
# keep this function call here  
# to see how to enter arguments in Python scroll down
print NumberSearch(raw_input())           
