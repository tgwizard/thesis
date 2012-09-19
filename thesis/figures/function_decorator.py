# function_decorator.py
# the function decorator
def decorator(decoratee):
	# define the closure ("inner function")
	def wrapper():
		print "before",
		# call the decorated function
		ret = decoratee()
		print "after",
		return ret
	# return the closure
	return wrapper
