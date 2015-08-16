from app import api
from shiftpy.wsgi_utils import envify

application = envify(api)
