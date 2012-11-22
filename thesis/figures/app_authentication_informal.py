from pythonrv import rv
from django.core.handlers.base import BaseHandler
# disable copying to work around bug in django
rv.configure(enable_copy_args=False)

# monitor the main request-processing method that
# has access to both the request and the response
@rv.monitor(bh=BaseHandler.get_response)
@rv.spec(when=rv.POST)
def ensure_auth(event):
  request = event.called_function.inputs[1]
  response = event.called_function.result
  if requires_auth(request, response):
    assert (request.user.is_authenticated(),
      "The current user is not authenticated")
    assert (request.user.is_active,
      "The current user is not active")

# a helper function for when authentication is
# required
def requires_auth(req, res):
  # only ok responses need authentication
  if res.status_code != 200:
    return False
  # requests to /login does not require auth nor
  # does /appmedia, which  is only css and images
  if (req.path.startswith("/login") or
      req.path.startswith("/appmedia")):
    return False
  return True
