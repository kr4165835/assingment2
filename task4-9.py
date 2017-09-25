def is_anagram(x,y):
	p=list(x)
	q=list(y)
	p.sort()==q.sort()
	return True
print(is_anagram('aaaaawp','waaaaap'))	
