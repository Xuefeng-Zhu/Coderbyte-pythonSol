def turn_minutes(time):
  result = time[:-2].split(":") 
  result = [int(result[0]), int(result[1])] if time[-2:] == "AM" else [int(result[0])+12, int(result[1])]
  result[0] = result[0] if (result[0]!=12 and result[0]!=24) else result[0]-12
  return result[0] * 60 + result[1]

def MostFreeTime(strArr): 
  times_list = []
  for time in strArr:
    times_list.append([turn_minutes(i) for i in time.split("-")])
  times_list.sort()
  most_free =  0
  for i in range(len(times_list)-1):
  	if times_list[i+1][0] - times_list[i][1] > most_free:
  		most_free =  times_list[i+1][0] - times_list[i][1]
  return "%02d:%02d" %(most_free/60, most_free%60) 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MostFreeTime(raw_input())           
