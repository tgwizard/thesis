from pythonrv import rv
from intranet.employee.models import Employee
from intranet import views

@rv.monitor(status=Employee.set_status, start=views.index)
@rv.spec(when=rv.POST)
def ensure_status_update_displayed(event):
  if event.fn.status.called:
    status_message = str(event.fn.status.inputs[1])
    def on_next_start(event):
      assert status_message in event.fn.start.result.content, \
        "New status not on start page"
    event.fn.start.next(on_next_start)
