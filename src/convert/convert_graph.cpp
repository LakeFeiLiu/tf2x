#include "convert_graph.h"
#include "pass_manager.h"

namespace tensorflow {
namespace tf2x {
namespace convert {
  // convert the GraphDef to x GraphDef
  tensorflow::Status ConvertGraphDefToXGraph(const tensorflow::GraphDef &graph_def,
    tensorflow::GraphDef *out_graph_def) {
      //tensorflow::GraphDef gdef;
      out_graph_def->CopyFrom(graph_def);
      //out_graph_def = &graph_def;
      return tensorflow::Status::OK();
    }
} // tensorflow
} // tf2x
} // convert

