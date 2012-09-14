from pythonrv import rv
import fibmodule

@rv.monitor(func=fibmodule.fib)
def spec(event):
	assert event.fn.func.inputs[0] > 0
