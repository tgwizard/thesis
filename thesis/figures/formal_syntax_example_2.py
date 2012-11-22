from pythonrv import rv
from pythonrv.formalrv import (formal_spec,
  make_assert, make_next, make_if)
import mymodule

@rv.monitor(foo=mymodule.foo,
	bar=mymodule.bar)
@formal_spec
def spec():
  # create assert specification
  a = make_assert(
          lambda event: event.fn.foo.called)

  # create if-then specification, with guard expression
  # and an assert specification in the then clause
  if_guard = lambda event: event.fn.foo.inputs[0] == 0
  if_then = make_assert(
          lambda event: event.fn.foo.inputs[1] == 0)
  i = make_if(if_guard, if_then)

  # create next specification
  n = make_next(spec_bar_called)
  # combine the three by tail composition
  return a + i + n

def spec_bar_called():
  # create assert specification
  a = make_assert(
          lambda event: event.fn.bar.called)
  # create next specification
  n = make_next(spec)
  # combine by tail composition
  return a + n
