#ifndef CONVERT_CONVERT_GRAPH_H_
#define CONVERT_CONVERT_GRAPH_H_
#include "tensorflow/core/framework/graph.pb.h"
#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/platform/types.h"

namespace tensorflow {
namespace tf2x {
namespace convert {
  tensorflow::Status ConvertGraphDefToXGraph(const tensorflow::GraphDef &,
    tensorflow::GraphDef *);
}
}
}

#endif