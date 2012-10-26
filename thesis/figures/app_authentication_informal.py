from pythonrv import rv
# disable copying to work around bug in django
rv.configure(enable_copy_args=False)

# monitor the main request-processing method that
# has access to both the request and the response
from django.core.handlers.base import BaseHandler
@rv.monitor(bh=BaseHandler.get_response)
def ensure_auth(event):
  request = event.called_function.inputs[1]
  response = event.called_function.result
  # only ok responses need authentication
  if response.status_code == 200:
    # requests to /login does not require auth
    # /appmedia is only css and images
    if not (request.path.startswith("/login") or
        request.path.startswith("/appmedia")):
        assert (request.user.is_authenticated(),
          "The current user is not authenticated")
        assert (request.user.is_active,
          "The current user is not active")
