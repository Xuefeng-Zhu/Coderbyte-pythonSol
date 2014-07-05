# Using the Python language, have the function ThirdGreatest(strArr) take the array of strings stored in strArr and return the third largest word within in. So for example: if strArr is ["hello", "world", "before", "all"] your output should be world because "before" is 6 letters long, and "hello" and "world" are both 5, but the output should be world because it appeared as the last 5 letter word in the array. If strArr was ["hello", "world", "after", "all"] the output should be after because the first three words are all 5 letters long, so return the last one. The array will have at least three strings and each string will only contain letters. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

# def ThirdGreatest(strArr): 
#   dStr = {}
#   for word in strArr:
#     dStr[len(word)] = dStr.get(len(word),[]) + [word]
#   temp = sorted(len(word) for word in strArr)
#   return dStr[temp[-3]][-1]

def ThirdGreatest(strArr): 
  return sorted([(word, -len(word)) for word in strArr], key=lambda x: x[1])[2][0]
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThirdGreatest(raw_input())  





