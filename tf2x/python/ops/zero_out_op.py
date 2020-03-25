from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import platform

if platform.system() != "Windows":
  from tensorflow.contrib.util import loader
  from tensorflow.python.platform import resource_loader
  _zero_engine_op = loader.load_op_library(
      resource_loader.get_path_to_datafile("libzeroout.so"))
else:
  raise RuntimeError("Windows platforms are not supported now")