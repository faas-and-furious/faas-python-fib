import sys

def fib(n):
	if n <= 1: return n
	else: return fib(n-1) + fib(n-2)

def handle(req):
	n = int(req)

	output = []
	for i in range(n):
		output.append(str(fib(i)))

	print(', '.join(output))
