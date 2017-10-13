
def euclidean(p, q):
	"""
	Euclidean distance finds the distance between two points in multidimensional space.
	"""
	sum_sq = 0.0

	# add up the squared differences
	for i in range(len(p)):
		sum_sq += pow(p[i] - q[i], 2)

	# return the square root of sum
	return pow(sum_sq, 0.5)

def pearson(p, q):
	"""
	The Pearson correlation coefficient is a measure of how highly correlated two variables are.
	The value lies between -1 and 1.
	"""
	n = len(p)
	vals = range(n)

	# simple sums
	sum_p = sum([float(p[i]) for i in vals])
	sum_q = sum([float(q[i]) for i in vals])

	# sum of squares
	sum_pSq = sum([float(p[i]**2 for i in vals)])
	sum_qSq = sum([float(p[i]**2 for i in vals)])
	
	# sum of products
	sum_pq = sum([float(p[i]) * float(q[i]) for i in vals])

	# Calculating the correlation coefficient
	num = sum_pq - (sum_q*sum_q / n)
	den = (sum_pSq * sum_qSq)**0.5
	coeff = num/den

	return coeff

def tanimoto(a, b):
	"""
	Tanimoto coefficient is another measure of similarity between two
	sets.
	"""
	c = [common for common in a if common in b]
	return float(len(c))/(len(a) + len(b) + len(c))

def gini_impurity(s):
	"""
	Gini impurity determines the impurity of our set.
	It tells us the probability of being wrong if we pick one item and 
	guess its label.
	"""
	total = len(s)
	counts = {}
	for item in s:
		counts.setdefault(item, 0)
		counts[item] += 1

	imp = 0
	for j in l:
		f1 = float(counts[j]/total)
		for k in l:
			if j==k: continue
			f2=float(counts[k])/total
			imp+=f1*f2
	return imp