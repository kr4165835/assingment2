def cumulative(b):
	y=[]
	my_sum=0
	for item in b:
		my_sum=my_sum+item
		y.append(my_sum)
	return y
print(cumulative([2,3,4]))
