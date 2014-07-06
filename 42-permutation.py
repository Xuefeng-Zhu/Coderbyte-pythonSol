def swap(nList,i):
  nList[i],nList[i-1] = nList[i-1], nList[i]
  for x in range(i, -1):
    if int(nList[i]) > int(nList[i+1]):
      nList[i],nList[i+1] = nList[i+1], nList[i]

def PermutationStep(num): 
  nList = list(str(num))
  for i in range(-1, -len(nList), -1):
    if int(nList[i]) > int(nList[i-1]):
      swap(nList,i)
      return "".join(nList)
  return -1
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PermutationStep(raw_input())  
















  