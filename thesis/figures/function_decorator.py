# function_decorator.py
# the function decorator
def cache(decoratee):
  decoratee.cache = dict()
  # define the closure ("inner function")
  def wrapper(x):
    if not x in decoratee.cache:
      # call the decorated function
      decoratee.cache[x] = decoratee(x)
    return decoratee.cache[x]
  return wrapper
