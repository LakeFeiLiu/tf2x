#include <pybind11/pybind11.h>

std::string convert_graph_to_x(std::string input) {
  return input;
}

PYBIND11_MODULE(wrap_conversion, m) {
  m.def("convert_graph_to_x", &convert_graph_to_x, "convert function");
}
