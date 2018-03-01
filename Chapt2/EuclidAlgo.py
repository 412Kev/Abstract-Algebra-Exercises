# Kevin Rhea Spring 2018
# Chapter 2 problem 3
# This program will compute the gcd of two positive integers
# it will also have find r and s such
#       gcd(a,b) = ra + sb


# function that computes gcd of two integers
# and returns r and s such -> gcd(a,b) = ra + sb
def ExtendedGcd(a ,b):
	# make sure a < b 
	if a < b: 
		t = b
		b = a
		a = t
	
	#inital values
	r,s = 0,1  
	u,v = 1,0

	#loop till a = 0 to find (gcd, r, s)
	while a != 0:
		q, r = b//a, b%a
		m, n = r - u*q, s - v*q

		#assign new values for next iteration
		b, a = a, r
		r, s = u, v
		u, v = m, n
	
	gcd = b
	return gcd, r, s

# function of recursive Euclidean Algoritgm 
def gcd(a ,b):
	# swap if a < b
	if a < b:
		t = b
		b = a
		a = t
	#find gcd
	if b == 0:
		return a
	return gcd(b, (a%b))


# Test out the functions
a = int(input('a = '))
b = int(input('b = '))

print(gcd(a,b))
print(ExtendedGcd(a,b))


