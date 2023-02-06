import environ
# from .settings import *

env = environ.Env()
# environ.Env.read_env()

# Project specific settings
if env("PROJECT_IN") == 'Production':
   from .production import *
else:
   from .development import *
