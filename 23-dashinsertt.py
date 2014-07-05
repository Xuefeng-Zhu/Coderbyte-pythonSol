def DashInsert(num):
  result = ""
  for i in str(num):
    if int(i)%2 == 0:
      result += i
    else:
      result += "-" + i
    return result 
    

# keep this function call here  
# to see how to enter arguments in Python scroll down
print DashInsert(raw_input())  
















  