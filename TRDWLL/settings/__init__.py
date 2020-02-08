from TRDWLL.settings.base import *

if os.environ['TRDWLL'] == 'prod':
   from .prod import *
else:
   from .dev import *