from pythonrv import rv
from pythonrv.formalrv import (formal_spec,
  make_assert, make_next)
import fibmodule

@rv.monitor(func=fibmodule.fib)
@formal_spec
def spec():
  a = make_assert(
          lambda event: event.fn.func.inputs[0] > 0)
  n = make_next(spec)
  return a + n
