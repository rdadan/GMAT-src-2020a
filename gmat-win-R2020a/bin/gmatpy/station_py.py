# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _station_py
else:
    import _station_py

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class doublep(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _station_py.doublep_swiginit(self, _station_py.new_doublep())
    __swig_destroy__ = _station_py.delete_doublep

    def assign(self, value):
        return _station_py.doublep_assign(self, value)

    def value(self):
        return _station_py.doublep_value(self)

    def cast(self):
        return _station_py.doublep_cast(self)

    @staticmethod
    def frompointer(t):
        return _station_py.doublep_frompointer(t)

# Register doublep in _station_py:
_station_py.doublep_swigregister(doublep)

def doublep_frompointer(t):
    return _station_py.doublep_frompointer(t)

class intp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _station_py.intp_swiginit(self, _station_py.new_intp())
    __swig_destroy__ = _station_py.delete_intp

    def assign(self, value):
        return _station_py.intp_assign(self, value)

    def value(self):
        return _station_py.intp_value(self)

    def cast(self):
        return _station_py.intp_cast(self)

    @staticmethod
    def frompointer(t):
        return _station_py.intp_frompointer(t)

# Register intp in _station_py:
_station_py.intp_swigregister(intp)

def intp_frompointer(t):
    return _station_py.intp_frompointer(t)

class stringp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _station_py.stringp_swiginit(self, _station_py.new_stringp())
    __swig_destroy__ = _station_py.delete_stringp

    def assign(self, value):
        return _station_py.stringp_assign(self, value)

    def value(self):
        return _station_py.stringp_value(self)

    def cast(self):
        return _station_py.stringp_cast(self)

    @staticmethod
    def frompointer(t):
        return _station_py.stringp_frompointer(t)

# Register stringp in _station_py:
_station_py.stringp_swigregister(stringp)

def stringp_frompointer(t):
    return _station_py.stringp_frompointer(t)

class boolp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _station_py.boolp_swiginit(self, _station_py.new_boolp())
    __swig_destroy__ = _station_py.delete_boolp

    def assign(self, value):
        return _station_py.boolp_assign(self, value)

    def value(self):
        return _station_py.boolp_value(self)

    def cast(self):
        return _station_py.boolp_cast(self)

    @staticmethod
    def frompointer(t):
        return _station_py.boolp_frompointer(t)

# Register boolp in _station_py:
_station_py.boolp_swigregister(boolp)

def boolp_frompointer(t):
    return _station_py.boolp_frompointer(t)

import gmatpy.gmat_py
class GroundStation(gmatpy.gmat_py.GroundstationInterface):
    r"""

    Defines the Groundstation class used to model ground based tracking stations.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _station_py.delete_GroundStation

    def __init__(self, *args):
        _station_py.GroundStation_swiginit(self, _station_py.new_GroundStation(*args))

    def Clone(self):
        return _station_py.GroundStation_Clone(self)

    def Copy(self, orig):
        return _station_py.GroundStation_Copy(self, orig)

    def GetParameterText(self, id):
        return _station_py.GroundStation_GetParameterText(self, id)

    def GetParameterUnit(self, id):
        return _station_py.GroundStation_GetParameterUnit(self, id)

    def GetParameterID(self, str):
        return _station_py.GroundStation_GetParameterID(self, str)

    def GetParameterType(self, id):
        return _station_py.GroundStation_GetParameterType(self, id)

    def GetParameterTypeString(self, id):
        return _station_py.GroundStation_GetParameterTypeString(self, id)

    def IsParameterReadOnly(self, *args):
        return _station_py.GroundStation_IsParameterReadOnly(self, *args)

    def GetStringParameter(self, *args):
        return _station_py.GroundStation_GetStringParameter(self, *args)

    def SetStringParameter(self, *args):
        return _station_py.GroundStation_SetStringParameter(self, *args)

    def GetStringArrayParameter(self, *args):
        return _station_py.GroundStation_GetStringArrayParameter(self, *args)

    def GetRealParameter(self, *args):
        return _station_py.GroundStation_GetRealParameter(self, *args)

    def SetRealParameter(self, *args):
        return _station_py.GroundStation_SetRealParameter(self, *args)

    def RenameRefObject(self, type, oldName, newName):
        return _station_py.GroundStation_RenameRefObject(self, type, oldName, newName)

    def GetRefObjectNameArray(self, type):
        return _station_py.GroundStation_GetRefObjectNameArray(self, type)

    def GetRefObject(self, type, name):
        return _station_py.GroundStation_GetRefObject(self, type, name)

    def SetRefObject(self, *args):
        return _station_py.GroundStation_SetRefObject(self, *args)

    def GetRefObjectArray(self, *args):
        return _station_py.GroundStation_GetRefObjectArray(self, *args)

    def HasRefObjectTypeArray(self):
        return _station_py.GroundStation_HasRefObjectTypeArray(self)

    def GetRefObjectTypeArray(self):
        return _station_py.GroundStation_GetRefObjectTypeArray(self)

    def Initialize(self):
        return _station_py.GroundStation_Initialize(self)

    def IsEstimationParameterValid(self, id):
        return _station_py.GroundStation_IsEstimationParameterValid(self, id)

    def GetEstimationParameterSize(self, id):
        return _station_py.GroundStation_GetEstimationParameterSize(self, id)

    def GetEstimationParameterValue(self, id):
        return _station_py.GroundStation_GetEstimationParameterValue(self, id)

    def IsValidID(self, id):
        return _station_py.GroundStation_IsValidID(self, id)

    def IsValidElevationAngle(self, state_sez):
        return _station_py.GroundStation_IsValidElevationAngle(self, state_sez)

    def CreateErrorModelForSignalPath(self, spacecraftName, spacecraftId):
        return _station_py.GroundStation_CreateErrorModelForSignalPath(self, spacecraftName, spacecraftId)

    def GetErrorModelMap(self):
        return _station_py.GroundStation_GetErrorModelMap(self)

    def HasLocalClones(self):
        return _station_py.GroundStation_HasLocalClones(self)
    STATION_ID = _station_py.GroundStation_STATION_ID
    ADD_HARDWARE = _station_py.GroundStation_ADD_HARDWARE
    IONOSPHERE_MODEL = _station_py.GroundStation_IONOSPHERE_MODEL
    TROPOSPHERE_MODEL = _station_py.GroundStation_TROPOSPHERE_MODEL
    DATA_SOURCE = _station_py.GroundStation_DATA_SOURCE
    TEMPERATURE = _station_py.GroundStation_TEMPERATURE
    PRESSURE = _station_py.GroundStation_PRESSURE
    HUMIDITY = _station_py.GroundStation_HUMIDITY
    MINIMUM_ELEVATION_ANGLE = _station_py.GroundStation_MINIMUM_ELEVATION_ANGLE
    ERROR_MODELS = _station_py.GroundStation_ERROR_MODELS
    GroundStationParamCount = _station_py.GroundStation_GroundStationParamCount

    @staticmethod
    def SetClass(base):
        return _station_py.GroundStation_SetClass(base)

# Register GroundStation in _station_py:
_station_py.GroundStation_swigregister(GroundStation)

def GroundStation_SetClass(base):
    return _station_py.GroundStation_SetClass(base)



