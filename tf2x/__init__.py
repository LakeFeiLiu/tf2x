from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.framework import errors
try:
  from tf2x.python import *
except errors.NotFoundError as e:
  no_message = (
    '*** Failed to initialize tf2x. This is either because the tf2x'
    ' installation path is not in LD_LIBRARY_PATH, or because you do not have'
    ' it installed. If not installed , please go to TODO : tf2x ***')
  print(no_message)
  raise e