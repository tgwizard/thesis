from pythonrv import rv
from pythonrv.formalrv import (formal_spec,
  make_assert, make_next, make_if)
import mymodule

@rv.monitor(foo=mymodule.foo,
	bar=mymodule.bar)
@formal_spec
def spec():
  a = make_assert(
          lambda event: event.fn.foo.called)

  if_guard = lambda event: event.fn.foo.inputs[0] == 0
  if_then = make_assert(
          lambda event: event.fn.foo.inputs[1] == 0)
  i = make_if(if_guard, if_then)

  n = make_next(spec_bar_called)
  return a + i + n

def spec_bar_called():
  a = make_assert(
          lambda event: event.fn.bar.called)
  n = make_next(spec)
  return a + n
