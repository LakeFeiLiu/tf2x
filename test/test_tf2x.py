#import example as tf2x
from sys import version_info
if version_info >= (2,6,0):
    def import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('wrap_conversion', [dirname(__file__)])
        except ImportError:
            import wrap_conversion
            return wrap_conversion
        if fp is not None:
            try:
                _mod = imp.load_module('wrap_conversion', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _wrap_conversion = import_helper()
    del import_helper
else:
    import wrap_conversion
del version_info
try:
    _property = property
except NameError:
    pass

