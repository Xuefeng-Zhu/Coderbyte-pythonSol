def is_Prime(n):
	for i in xrange(3, int(n ** 0.5)+1, 2):
		if n % i == 0:
			return False
	return True
	
def PrimeMover(num): 
	count = 1 
	i = 1
	while count < num:
		i += 2
		if is_Prime(i):
			count += 1
	return i


# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeMover(raw_input())  
