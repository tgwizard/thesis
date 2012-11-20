from pythonrv import rv
class CustomErrorHandler(object):
    def handle(self, level, errors):
        if level == rv.CRITICAL:
            # raise only the first error
            raise errors[0]

rv.configure(error_handler=CustomErrorHandler())

@rv.monitor(...)
@rv.spec(level=rv.CRITICAL)
def spec(event):
    assert False
