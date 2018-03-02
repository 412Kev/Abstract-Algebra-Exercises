# Kevin Rhea
# Chapter 4 problem 1
# This program will take in a number
# and output as a sum of distinct powes of 2

def pow2(n):
	binary = bin(n)[:1:-1] #This is the binary of n reversed
	sumOf2 = ""
	x = 0
	for exp in binary:
		if exp == '1':
			sumOf2 += "2^" + str(x) +  " "
		x += 1
	return sumOf2

num = int(input("Enter a number: "))
print("As a power of 2 your number is")
print(pow2(num))