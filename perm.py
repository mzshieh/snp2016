def f(n,d=0,perm=[]):
	if n==d:
		yield perm
	else:
		for _ in range(n):
			if perm.count(_)==0:
				perm.append(_)
				for __ in f(n,d+1,perm):
					yield __
				perm.pop()

x = f(5)
print(next(x))
print(next(x))
print(next(x))
