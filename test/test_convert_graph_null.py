import tf2x
import tensorflow as tf
from tensorflow.python.platform import gfile

with gfile.FastGFile('./simple_model.pb') as f:
  graph_def = tf.GraphDef()
  graph_def.ParseFromString(f.read())
  tf.import_graph_def(graph_def, name="")

sess = tf.Session()
tf.train.write_graph(sess.graph_def, './', 'simple_model.pbtxt', as_text=True)
x = sess.graph.get_tensor_by_name('x:0')
y = sess.graph.get_tensor_by_name('y:0')
out = sess.graph.get_tensor_by_name('op_to_store:0')


result = sess.run(out, {x: 10, y: 3})
print("result is ", result)

