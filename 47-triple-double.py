def check(num, target):
  result = set()
  number = 0
  count = 0
  for i in str(num):
    if i == number:
      count += 1
      if count == target:
        result.add(number)
    else:
      number = i
      count = 1
  return result 

def TripleDouble(num1,num2): 
  temp1 = check(num1, 3)
  temp2 = check(num2, 2)
  return 1 if temp1 & temp2 else 0
# keep this function call here  
# to see how to enter arguments in Python scroll down
print TripleDouble(raw_input())  
















  