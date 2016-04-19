from .base_settings import *

try:
    from .production import *
except:
    pass
 
try:
    from .local import *
except:
    pass