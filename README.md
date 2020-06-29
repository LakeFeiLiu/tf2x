# tf2x
A project for a DL compiler integrating with TensorFlow.

The project can convert the whole graph to subgraphs and call the DL compiler for each subgraph.

## build

dependence : 1. TensorFlow and its dependence; 2. PyBind11

1. auto build
     sh build.sh
2. manual build
     python setup.py bdist_wheel

## test

1. test the "zeroout" example

   python test/test_run.py

2. test the convert.

   python test/test_convert.py