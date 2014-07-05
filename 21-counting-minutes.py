def turn24H(time):
  result = time[:-2].split(":") 
  result = [int(result[0]), int(result[1])] if time[-2:] == "am" else [int(result[0])+12, int(result[1])]
  result[0] = result[0] if (result[0]!=12 and result[0]!=24) else result[0]-12
  return result

def CountingMinutesI(str): 
  time1,time2 = [turn24H(time) for time in str.split("-")]
  if (time1[0] < time2[0]):
  	return 60* (time2[0] - time1[0]) + time2[1] - time1[1]
  else:
  	return 60 * (24 - time1[0] + time2[0]) - time1[1] + time2[1] 

# keep this function call here  
# to see how to enter arguments in Python scroll down
print CountingMinutesI(raw_input())  


