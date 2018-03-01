# Kevin Rhea Spring 2018
# Chapter 2 problem 1
# The Sieve of Eratosthenes: Computes the all the primes less than a number N
# Problem asks
	# Find all prime number less than n: when n is 250
	# Find all relatively prime for n

from math import sqrt,floor

# Find primes less than n using Sieve of Eratosthenes method
def primes(n):
	#Put all i in a list such 0 < i < n
	lessN = []
	for i in range (1,n-1):
		lessN.append(int(i))

	#Remove multiples of i from list for all 2 < i < sqrt(n)
	for i in range (2, floor(sqrt(n))):
		for j in range (2, n):
			if (i*j) in lessN:
				lessN.remove(i*j)
	return lessN

# Find relatively prime numbers to n using similar method as above
def rprimes(n):
	prime = primes(n)

	lessN = []
	for i in range (2,n-1):
		lessN.append(int(i))

	#Remove multiples of i from list for all 2 < i < sqrt(n)
	for p in prime:
		if n%p == 0 and p > 1:
			for j in range (floor(n/2)):
				if (p*j) in lessN:
					lessN.remove(p*j)
	return lessN

# Test functions
print('Primes less than 250')
print(primes(250))
print()
print()
print('Relatively prime numbers to 250')
print(rprimes(250))