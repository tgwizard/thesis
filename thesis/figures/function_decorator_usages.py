# test.py
from function_decorator import cache

def fact(x):
  if x <= 1:
    return 1
  return x*fact(x-1)

print fact(5) # >> 120 (5 calls to fact)
print fact(5) # >> 120 (5 calls to fact)

# decorate fact2
# equivalent to fact2 = cache(fact)
@cache
def fact2(x):
  if x <= 1:
    return 1
  return x*fact2(x-1)

print fact2(5) # >> 120 (5 calls to fact2, results cached)
print fact2(5) # >> 120 (0 calls to fact2)
