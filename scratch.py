import os
import numpy
import ctypes


print(ctypes.__file__)


numpy_path = os.path.dirname(numpy.__file__)

print (numpy_path)