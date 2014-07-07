# Using the Python language, have the function PrimeChecker(num) take num and return 1 if any arrangement of num comes out to be a prime number, otherwise return 0. For example: if num is 910, the output should be 1 because 910 can be arranged into 109 or 019, both of which are primes. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.
def is_Prime(n):
	if n % 2 == 0:
		return False
	for i in xrange(3, int(n ** 0.5)+1, 2):
		if n % i == 0:
			return False
	return True
  
import itertools
def PrimeChecker(num): 
  temp = str(num)
  for num in itertools.permutations(temp, len(temp)):
    if is_Prime(int("".join(num))):
      return 1
  return 0  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeChecker(raw_input())  