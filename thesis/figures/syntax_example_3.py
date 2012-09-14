from pythonrv import rv
import mymodule

@rv.monitor(foo=mymodule.foo,
	bar=mymodule.bar,
	baz=mymodule.baz)
def spec(event):
	if event.fn.foo.called:
		# add function to be called on next event
		event.fn.foo.next(followup)
		event.finish()
	else:
		# verification has failed
		# same as assert False
		event.failure()

def followup(event):
	if event.fn.bar.called:
		event.success()
	elif event.fn.baz.called:
		assert event.fn.baz.inputs[0] == true
		# call this function on next event as well
		event.fn.foo.next(followup)
	else:
		event.failure()

