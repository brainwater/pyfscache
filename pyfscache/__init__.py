#! /usr/bin/env python

'''
pyfscache: A file system cache for python.
Copyright (c) 2013, James C. Stroud; All rights reserved.

This forked version modified by Robert Clewley.
'''

from . _version import __version__

from . fscache import *
from . import tests

__all__ = ["FSCache", "make_digest",
           "auto_cache_function", "cache_function", "to_seconds"]
