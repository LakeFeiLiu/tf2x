#include "pass_manager.h"

namespace tensorflow {
namespace tf2x {
namespace convert {

std::vector<Pass>& getCustomPasses() {
  static std::vector<Pass> passes;
  return passes;
}

RegisterPass::RegisterPass(Pass p) {
  getCustomPasses().emplace_back(std::move(p));
}

} // convert
} // namespace tf2x
} // namespace tensorflow