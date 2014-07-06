import itertools 
def ArrayAddition(arr): 
  maxN = max(arr)
  for i in range(2, len(arr)):
    for item in itertools.combinations(arr,i):
      if sum(item)==maxN:
        return "true"
  return "false"
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArrayAddition(raw_input())  
















  