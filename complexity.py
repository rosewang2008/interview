# Time Complexity
# Big O:  upper bound on time
# Big omega: lower bound
# Big theta: both big omega and big O, tight bound

# Space Complexity

def sum(n):
	'''n should be a positive integer, else return 0 
	'''
	# O(n) time and O(n) space
	if n <= 0:
		return 0
	else:
		return n + sum(n - 1)

print(sum(3))

def pairSumSequence(n):
	'''add integers less than or equal to n in pairs.
	'''
	total = 0
	for i in range(n):
		total += pairSum(i, i + 1)
	return total

def pairSum(a, b):
	'''adds two integers together
	'''
	return a + b

print(pairSumSequence(3))

# Drop constants, non dominant terms
# multi-part algorithms

# Amortized Time




# Log(n) runtimes
def binarySearch(n, x):
	''' n is a list that contains an element x.
	'''
	middle_index = len(n)//2 #how to do upper bound
	if n[middle_index] == x:
		return x
	elif x < n[middle_index]:
		return binarySearch(n[:middle_index], x)
	else:
		return binarySearch(n[middle_index:],x)

print(binarySearch([1,3,4,5], 3))

# base of log: doesn't matter
# how many times can you multiply by 2 until we get N?

# recursive runtimes

# Hash Tables



			