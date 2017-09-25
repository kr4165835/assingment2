
def cpatalize_all(a):
	x=a.upper() 
		
	return x		

def capatal(p):
	y=[]
	for item in p:
		if isinstance(item , list):
			item=capatal(item)
		else:
			item=cpatalize_all(item)
			y.append(item)
	return y
q=(b(['a','b',['c','d']]))
print(q)
