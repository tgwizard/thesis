from pythonrv import rv
from pythonrv.formalrv import (formal_spec,
  make_assert, make_next)
import fibmodule

@rv.monitor(func=fibmodule.fib)
@formal_spec
def spec():
  # create assert specification
  a = make_assert(
          lambda event: event.fn.func.inputs[0] > 0)
  # create next specification
  n = make_next(spec)
  # combine by composition
  return a + n
