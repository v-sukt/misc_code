primeNos = [1]

for i in range(2, 100000):
	# print(i)
	count=2
	# print("count init")
	while i % count != 0 and count < i:
		count = count+1
		# print("count incr.")
		# print("coint",count)

	if i == count:
		primeNos.append(i)

print(f"prime nos: {primeNos}")
"""
real    1m26.425s
user    1m25.863s
sys     0m0.111s
"""
