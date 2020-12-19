# __init__.py for GMAT Python API

import os, platform

filePath = os.path.dirname(os.path.abspath(__file__))
binPath = os.path.split(filePath)[0]

if platform.system() == "Windows":
    from ctypes import cdll

    cdll.LoadLibrary(os.path.normpath(os.path.join(binPath, "libGmatUtil")))
    cdll.LoadLibrary(os.path.normpath(os.path.join(binPath, "libGmatBase")))
    cdll.LoadLibrary(os.path.normpath(os.path.join(binPath, "../plugins/libStation")))
    cdll.LoadLibrary(os.path.normpath(os.path.join(binPath, "../plugins/libGmatEstimation")))

    del cdll
del platform

__all__ = ["gmat_py", "station_py", "navigation_py"]

from .gmat_py import *
from .station_py import *
from .navigation_py import *

fileManager = gmat_py.FileManager.Instance()
fileManager.SetBinDirectory("gmatpy/gmat_py.py", binPath + os.sep)
