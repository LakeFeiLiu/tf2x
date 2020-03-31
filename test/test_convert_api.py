import tf2x
input_str = "input graph"
print(dir(tf2x.convert_graph_test()))
output_str = tf2x.convert_graph_test(input_str)
print("result is ", output_str)

