#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include "convert/pybind_api.h"

namespace py = pybind11;
PYBIND11_MODULE(wrap_conversion, m) {
  m.def("convert_graph_to_x", &tensorflow::tf2x::convert::convert_graph_to_x, 
    py::return_value_policy::reference, "convert function");
}
