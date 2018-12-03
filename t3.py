def super_dec(some_var):	
	def decorator_func(original_func):
		def wrapper_func(*args):
			print("wrapping up", original_func.__name__ , "using super decorator", some_var)
			return original_func(*args)
		return wrapper_func
	return decorator_func

@super_dec("*** testing with 3 variables ***")
def some_func1(a,b,c):
	print("this is just some function")
	print(a+b+c)

@super_dec("*** 0 variables here ***")
def some_func2():
	print("just the other function")

some_func1(1,2,3)

some_func2()