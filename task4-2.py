import functools
x=list(range(100,500,2))
y=lambda a,b:a+b
z=funtools.reduce(y,x)
print(z)


