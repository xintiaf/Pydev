try:
    from _pydevd_bundle.pydevd_cython import trace_dispatch, PyDBAdditionalThreadInfo
except ImportError:
    try:
        import struct
        import sys
        is_python_64bit = (struct.calcsize('P') == 8)
        plat = '32'
        if is_python_64bit:
            plat = '64'

        # We also accept things as:
        #
        # _pydevd_bundle.pydevd_cython_win32_27_32
        # _pydevd_bundle.pydevd_cython_win32_34_64
        #
        # to have multiple pre-compiled pyds distributed along the IDE.

        mod_name = 'pydevd_cython_%s_%s%s_%s' % (sys.platform, sys.version_info[0], sys.version_info[1], plat)
        check_name = '_pydevd_bundle.%s' % (mod_name,)
        mod = __import__(check_name)
        mod = getattr(mod, mod_name)
        trace_dispatch, PyDBAdditionalThreadInfo = mod.trace_dispatch, mod.PyDBAdditionalThreadInfo
    except ImportError:
        raise