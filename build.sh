#! /bin/sh

rm -rf build tf2x.egg-info
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
python setup.py bdist_wheel
echo 'y' | pip uninstall dist/tf2x-0.0.1-cp27-cp27mu-linux_x86_64.whl
pip install dist/tf2x-0.0.1-cp27-cp27mu-linux_x86_64.whl
