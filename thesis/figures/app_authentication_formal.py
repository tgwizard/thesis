from pythonrv import rv
from pythonrv.formalrv import formal_spec, make_if, make_assert
from django.core.handlers.base import BaseHandler
# disable copying to work around bug in django
rv.configure(enable_copy_args=False)

@rv.monitor(bh=BaseHandler.get_response)
@formal_spec
def ensure_auth(event):
  auth = make_assert(lambda e:
      e.called_function.inputs[1].user.is_authenticated())
  active = make_assert(lambda e:
      e.called_function.inputs[1].user.is_active)

  return make_if(requires_auth, auth + active)

def requires_auth(event):
  return event.called_funcion.result.status_code == 200 and \
      not event.called_function.inputs[1].path.startswith("/login") and \
      not event.called_function.inputs[1].path.startswith("/appmedia")
