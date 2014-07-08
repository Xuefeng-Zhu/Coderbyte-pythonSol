import sys
def CoinDeterminer(num): 
  coins = [11, 9, 7, 5, 1]
  count = sys.maxint
  for i in range(len(coins)):
    tCount = 0
    tNum = num
    for j in range(i, len(coins)):
      tCount += tNum / coins[i]
      tNum = tNum % coins[i]
    if tCount < count:
      count = tCount 
  return count   
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print CoinDeterminer(raw_input())           
