import os
from setuptools import setup, Command
from setuptools.extension import Extension
from Cython.Build import cythonize
import platform
import numpy

import sys

extensions = [
    Extension("kerrpy_cython.geodesic_integrator", ["kerrpy_cython/geodesic_integrator.pyx"],
              define_macros = [('CYTHON_TRACE', '1')],
              include_dirs=[numpy.get_include()]),
    # Extension("raytracer", ["kerrpy_cython/raytracer.pyx"],
    #           include_dirs=[numpy.get_include()]),
    Extension("kerrpy_cython.metric", ["kerrpy_cython/metric.pyx"],
              define_macros = [('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')],
              include_dirs=[numpy.get_include()]),
    Extension("kerrpy_cython.initial_setup", ["kerrpy_cython/initial_setup.pyx"],
              define_macros = [('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')],
              libraries=["m"],
              extra_compile_args=["-O3", "-ffast-math", "-march=native"],
              include_dirs=[numpy.get_include()]),
]

common_includes = ["kerrpy_cython/_common/*.pyx"]

setup(
    name="kerrpy_cython",
    ext_modules=cythonize(extensions + common_includes,compiler_directives={'linetrace': True}),
)
