def gcd(a, b):
	while a != 0 and b != 0:
		if a < b:
			a, b = b, a
		a %= b
	return a + b


a, b = map(int, input().split())
res = gcd(a, b)