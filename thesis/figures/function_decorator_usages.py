# test.py
from function_decorator import decorator

def func_a():
	print "a"

func_a()
# output:
#		a

# decorate func_a
func_a = decorator(func_a)
func_a()
# output:
# 	before
#		a
#		after

# decorate func_b - equivalent
# to the decoration of func_a
@decorator
def func_b():
	print "b"

func_b()
# output:
# 	before
#		b
#		after
