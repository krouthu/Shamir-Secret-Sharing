# Keerthana Routhu
# krouthu
# Assignment 1 - Breaking the Vault
# When I run the test script, I get an "Interpolated value from points 
# incorrect" error. When I posted about this on Piazza, Eugene said 
# he ran my code and it worked fine. Thank you!

from fractions import Fraction
import random
import math

def split (val, n, k):
	i = 1
	j = 0
	l = 0
	function = [Fraction(val)]
	xVals = []
	yVals = []
	coordinates = []

	for i in range(k):
		function.append(Fraction(random.randint(1,100)))
	for j in range(n):
		xVals.append(Fraction(random.randint(1,100)))
	for l in range(n):
		m = 0
		temp = 0
		for m in range(k):
			temp += (math.pow(xVals[l], m) * function[m])
		yVals.append(temp)
	coordinates = zip(xVals,yVals)
	return coordinates

def interpolate (points, x):
	xVals, yVals = zip(*points)
	vals = Fraction(0)
	i = 0
	for i in range(len(xVals)):
		numerator = Fraction(1)
		denominator = Fraction(1)
		j = 0
		for j in range(len(xVals)):
			if (j != i):
				numerator *= Fraction((x-xVals[j]))
				denominator *= Fraction((xVals[i]-xVals[j]))
		vals += (Fraction(yVals[i])*Fraction(numerator,denominator))
	return vals
