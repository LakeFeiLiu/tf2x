#include "pybind_api.h"
#include "tensorflow/core/lib/core/errors.h"
#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/framework/graph.pb.h"

#include "convert_graph.h"

namespace tensorflow {
namespace tf2x {
namespace convert {
  // for python api convert
  std::pair<std::string, std::string> convert_graph_to_x(std::string graph_def_str) {
    tensorflow::GraphDef graph_def;
    std::string out_status;
    if (!graph_def.ParseFromString(graph_def_str)) {
      out_status = "Invalid Argument; Could not interpret input as a GraphDef";
      return std::pair<std::string, std::string>{out_status, ""};
    }

    //convert the graph to xgraph
    tensorflow::GraphDef outGraph;
    tensorflow::Status convert_status =
      tensorflow::tf2x::convert::ConvertGraphDefToXGraph(graph_def, &outGraph);
    if (!convert_status.ok()) {
      auto retCode = (int)convert_status.code();
      char buff[2000];
      snprintf(buff, 2000, "%d;%s", retCode,
        convert_status.error_message().c_str());
      out_status = buff;
      return std::pair<std::string, std::string>{out_status, ""};
    }
    std::string result;
    if (!outGraph.SerializeToString(&result)) {
      out_status = "InVaildArgument; Could not serialize output as a GraphDef";
      return std::pair<std::string, std::string>{out_status, ""};
    }
    out_status = "OK;All good";
    return std::pair<std::string, std::string>{out_status, result};
  }

} // tensorflow
} // tf2x
} // convert