import sys

def fib(n):
	if n <= 1: return n
	else: return fib(n-1) + fib(n-2)

for line in sys.stdin:
	n = int(line.strip())

	output = []
	for i in range(n):
		output.append(str(fib(i)))
	print(', '.join(output))
