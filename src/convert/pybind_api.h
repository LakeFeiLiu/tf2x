#ifndef CONVERT_PYBIND_API_H_
#define CONVERT_PYBIND_API_H_
#include <utility>
#include <string>

namespace tensorflow {
namespace tf2x {
namespace convert {
  std::pair<std::string, std::string> convert_graph_to_x(std::string);
}
}
}

#endif