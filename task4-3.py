import functools
my_list=list(range(0,10,2))

y=lambda a,b:a+b*b

z=reduce(y,my_list)
print(z)

