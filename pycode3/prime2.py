primeNo = [1]

for i in range(2, 100000):
	j = 2
	counter = 0
	while j < i:
		if i % j == 0:  # its divisble completely by no. less than itself
			counter = 1
			j = j + 1
		else:
			j = j + 1
	if counter == 0:
		primeNo.append(i)
	else:
		counter = 0

print(f"prime nos: {primeNo}")

"""
real    13m52.659s
user    13m50.296s
sys     0m0.988s
"""
