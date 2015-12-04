def combination(n, r):
	if n == r:
		return 1
	elif n > 1 and r > 1:
		return combination(n-1, r) + combination(n-1, r-1)
	elif r == 1:
		return n

print( combination(40,10) )
