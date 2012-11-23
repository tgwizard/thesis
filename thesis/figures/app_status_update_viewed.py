from pythonrv import rv
from pythonrv.formalrv import (formal_spec,
  make_assert, make_next, make_if)
from intranet.employee.models import Employee
from intranet import views

@rv.monitor(status=Employee.set_status, start=views.index)
@formal_spec
def must_view_status_update():
  must_view = make_assert(
      lambda e: (e.fn.start.called, "Didn't view status update"))
  if_updated = make_if(
      lambda e: e.fn.status.called, make_next(must_view))
  spec = if_updated + make_next(lambda: spec)
  return spec
