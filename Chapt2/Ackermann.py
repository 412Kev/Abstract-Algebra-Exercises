# Kevin Rhea Spring 2018
# Ackermann function are defined by 
# 1. A(0,y) = y + 1
# 2. A(x+1, 0) = A(x,1)
# 3. A(x+1, y+1) = A(x, A(x+1,y))
# This program will make Ackermann function and compute A(3,1)

# The ackermann function based off the equations given in the problem
def ackermann(x,y):
	if (x+y) == 0:
		return 1
	if (x+y) == 1:
		return 2
	if x == 0:
		return (y+1)
	if y == 0:
		return ackermann((x-1), 1)
	return ackermann((x-1), ackermann(x, (y-1)))

print(ackermann(1,3))