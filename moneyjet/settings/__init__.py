from .base_settings import *
from .passwd import *

try:
    from .production import *
except:
    pass
 
try:
    from .local import *
except:
    pass