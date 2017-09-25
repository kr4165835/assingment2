list1=[2,5,6,[1,3]]
def nested_sum(x):
	sums=0
	for i in x:
		if isinstance(i, list):
			sums = sums+nested_sum(i)
		else:
			sums= sums+ i
	return sums
print(nested_sum(list1))
