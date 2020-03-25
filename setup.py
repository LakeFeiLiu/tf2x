import os
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools import find_packages

FILE_DIR = os.path.realpath(os.path.dirname(__file__))

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir], cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.'], cwd=self.build_temp)
        print('build_temp=', self.build_temp)
        CMAKE_BUILD_DIR = os.path.join(FILE_DIR, self.build_temp)
        print('cmake dir=', CMAKE_BUILD_DIR)

        for ext in self.extensions:
            # copy the wrap_conversion.so file
            src = os.path.join(CMAKE_BUILD_DIR, "wrap_conversion.so")
            dst = os.path.join(FILE_DIR, "tf2x")
            print("src=", src)
            print("dst=", dst)
            if not os.path.exists(os.path.dirname(dst)):
                os.makedirs(os.path.dirname(dst))
            self.copy_file(src, dst)
            # copy the example op .so file
            src = os.path.join(CMAKE_BUILD_DIR, "libzeroout.so")
            dst = os.path.join(FILE_DIR, "tf2x/python/ops")
            print("src=", src)
            print("dst=", dst)
            if not os.path.exists(os.path.dirname(dst)):
                os.makedirs(os.path.dirname(dst))
            self.copy_file(src, dst)

setup(
    name='tf2x',
    version='0.0.1',
    author='Fei Liu',
    author_email='liufei8653@163.com',
    description='A really cool and easy to install library',
    long_description='',
    ext_modules=[CMakeExtension('.')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
    include_package_data=True,
    exclude_package_data={'':['setup.py']},
    packages=find_packages(),
    package_data={
      '':['*.so'] + ['python/ops/*.so'],
    },
)