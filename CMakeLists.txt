CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT(tfx2)

set(CMAKE_CXX_STANDARD 11)
SET(CMAKE_BUILD_TYPE "Debug")

if(CMAKE_COMPILER_IS_GNUCXX)
  add_compile_options(-D_GLIBCXX_USE_CXX11_ABI=0)
endif(CMAKE_COMPILER_IS_GNUCXX)

set(SRC_THIRD_PARTY ./third_party)

find_package(Python 2.7 COMPONENTS Interpreter Development)
message("Python_SITEARCH = ", ${Python_SITEARCH})
set(TF_DIR ${Python_SITEARCH}/tensorflow)
include_directories(${TF_DIR}/include)
link_directories(${TF_DIR})

AUX_SOURCE_DIRECTORY(./src SRC_FILES)
AUX_SOURCE_DIRECTORY(./src/convert SRC_FILES)
message("src file lists " ${SRC_FILES})

#get the pybind11 include path
execute_process(
  COMMAND python -m pybind11 --includes
  OUTPUT_VARIABLE PYBIND11_INCLUDES
)
message("pybind11 file lists " ${PYBIND11_INCLUDES})
string(REPLACE "\n" " " PYBIND11_INCLUDES ${PYBIND11_INCLUDES})


if(CMAKE_COMPILER_IS_GNUCXX)
  set(CMAKE_CXX_FLAGS "${PYBIND11_INCLUDES} ${CMAKE_CXX_FLAGS}")
endif(CMAKE_COMPILER_IS_GNUCXX)

add_library(wrap_conversion SHARED ${SRC_FILES})
set_target_properties(wrap_conversion
  PROPERTIES
  CXX_STANDARD 11
  CXX_STANDARD_REQUIRED ON
  PYTHON 2.7
)

target_link_libraries(wrap_conversion -ltensorflow_framework)


# compile the register Op for example
AUX_SOURCE_DIRECTORY(./src/kernel KERNEL_FILES)
add_library(zeroout SHARED ${KERNEL_FILES})
target_link_libraries(zeroout -ltensorflow_framework)


