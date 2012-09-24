from pythonrv import rv
import mymodule

@rv.monitor(foo=mymodule.foo,
	bar=mymodule.bar)
def spec(event):
	if event.fn.foo.called:
		# the foo function was called
		# either the size of the event history
		# is 1 - this is the first event - or
		# the previous event was a call to bar
		assert len(event.history) == 1 \
			or event.prev.fn.bar.called
	elif event.fn.bar.called:
		# the bar function was called
		# assert that previous event
		# was a call to foo
		assert event.prev.fn.foo.called
