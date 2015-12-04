def sum35(num):
	ans = 0
	for i in xrange(0, num, 3):
		ans += i
	for i in xrange(0, num, 5):
		ans += i
	for i in xrange(0, num, 15):
		ans -= i
	return ans
print("The sum of all the multiples of 3 or 5 below 1000 is " + str(sum35(1000)) + ".")
