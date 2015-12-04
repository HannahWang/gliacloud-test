def findMaxPrime(num):
	up = int(num**0.5)
	if prime(num):
		return num
	for i in xrange(2, up+1):
		if num%i == 0 and prime(i):
			return findMaxPrime(num/i)

def prime(num):	#find whether num is a prime
	up = int(num**0.5)
	for i in xrange(2, up):
		if num%i == 0:
			return False
	return True

print(findMaxPrime(600851475143))
