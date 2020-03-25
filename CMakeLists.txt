CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT(tfx2)

set(CMAKE_CXX_STANDARD 11)

set(SRC_THIRD_PARTY ./third_party)

AUX_SOURCE_DIRECTORY(./src SRC_FILES)
message("src file lists " ${SRC_FILES})

add_subdirectory(${SRC_THIRD_PARTY}/pybind11)
pybind11_add_module(wrap_conversion ${SRC_FILES})
set_target_properties(wrap_conversion
  PROPERTIES
  CXX_STANDARD 11
  CXX_STANDARD_REQUIRED ON
)


# compile the register Op for example
if(CMAKE_COMPILER_IS_GNUCXX)
  add_compile_options(-D_GLIBCXX_USE_CXX11_ABI=0)
endif(CMAKE_COMPILER_IS_GNUCXX)
#TF_INC=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())')
#TF_INC=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())')
#find_package(tensorflow 1.12.3 REQUIRED COMPONENTS python)
find_package(Python COMPONENTS Interpreter Development)
set(TF_DIR ${Python_SITEARCH}/tensorflow)
include_directories(${TF_DIR}/include)
link_directories(${TF_DIR})
AUX_SOURCE_DIRECTORY(./src/kernel KERNEL_FILES)
add_library(zeroout SHARED ${KERNEL_FILES})
target_link_libraries(zeroout -ltensorflow_framework)


