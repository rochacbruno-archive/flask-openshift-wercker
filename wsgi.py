from api import api
from shiftpy.wsgi_utils import envify

application = app = envify(api)
