class Comb:
	Cmap = []
	def combination(self, n, r):
		n_index = n-1
		r_index = r-1
		if not self.Cmap:
			tmp = []
			self.Cmap = [tmp]*(n)
			for i in xrange(n):
				tmp = []
				if i < r:
					self.Cmap[i] = [tmp]*(i+1)
				else:
					self.Cmap[i] = [tmp]*(r)
		if self.Cmap[n_index][r_index]:
			return self.Cmap[n_index][r_index]
		elif n == r:
			return 1
		elif n > 1 and r > 1:
			self.Cmap[n_index-1][r_index] = self.combination(n-1, r)
			self.Cmap[n_index-1][r_index-1] = self.combination(n-1, r-1)
			return self.Cmap[n_index-1][r_index] + self.Cmap[n_index-1][r_index-1]
		elif r == 1:
			return n

Cex = Comb()
print( Cex.combination(990,33) )
