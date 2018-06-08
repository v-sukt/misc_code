primeNo=[1]
for i in range(2,100000000000000):
	j=2	
	counter=0
	while j<i:
		if i%j == 0:#its divisble completely by no. less than itself
			counter=1
			j=j+1
		else:
			j=j+1
	if counter==0:
		primeNo.append(i)
	else:
		counter=0
for i in primeNo:
	print(i)
