primeNos=[1]
for i in range(2,10000):
#	print(i)
	count=2
#	print("count init")
	while i%count!=0 and count<i:
		count=count+1
#		print("count incr.")
#		print("coint",count)
	if i==(count):
		primeNos.append(i)	
print("prime nos:")
for i in primeNos:
	print(i)
