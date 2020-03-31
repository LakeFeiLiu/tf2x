from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tf2x.wrap_conversion import convert_graph_to_x
from tensorflow.core.framework import graph_pb2
from tensorflow.python.framework import errors_impl as errors_impl
import six as _six

def convert_graph_test(input_graph_def="null"):
  output = input_graph_def
  #output = convert_graph_to_x(input_graph_def)
  return output

def convert_xgraph(input_graph_def):
  def py2bytes(inp):
    return inp

  def py3bytes(inp):
    return inp.encode("utf-8", errors="surrogateescape")

  def py2string(inp):
    return inp.encode()

  def py3string(inp):
    return inp.decode("utf-8")

  if _six.PY2: 
    to_bytes = py2bytes
    to_string = py2string
  else:
    to_bytes = py3bytes
    to_string = py3string
  input_graph_def_str = input_graph_def.SerializeToString()
  out = convert_graph_to_x(input_graph_def_str)
  status = to_string(out[0])
  output_graph_def_str = to_string(out[1])
  del input_graph_def_str
  if len(status) < 2:
    raise _impl.UnknownError(None, None, status)
  if status[:2] != "OK":
    msg = status.split(";")
    if len(msg) == 1:
      raise RuntimeError("Status Message is malformed {}", format(status))
    raise _impl._make_specific_execption(None, None, ";".join(msg[1]),
                                                        int(msg[0]))
  output_graph_def = graph_pb2.GraphDef()
  output_graph_def.ParseFromString(output_graph_def_str)
  del output_graph_def_str
  return output_graph_def
