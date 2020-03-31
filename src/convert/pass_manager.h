#ifndef CONVERT_PASS_MANAGER_H_
#define CONVERT_PASS_MANAGER_H_

#include <tensorflow/core/graph/graph.h>

/* `getCustomPasses()` returns a vector of passes that will be executed after
 * differentiation but before any fusion.  This is the de-facto location
 * for compiler backends to insert passes.
 *
 * Static registration of a pass can be done by creating a global
 * `RegisterPass r(Pass)` variable in a compilation unit.
 *
 * pass_manager.h uses a Meyer's singleton
 * to store a vector of `Pass`es, which modify the IR graph in place.
 */

namespace tensorflow {
namespace tf2x {
namespace convert {

// A pass modifies a Graph in place.
using Pass = std::function<void(std::shared_ptr<tensorflow::Graph>&)>;

std::vector<Pass>& getCustomPasses();

struct RegisterPass {
  RegisterPass(Pass p);
};

} // convert
} // namespace tf2x
} // namespace tensorflow

#endif
