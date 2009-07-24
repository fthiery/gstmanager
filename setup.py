#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, imp
from distutils.core import setup

#gstmanager = imp.load_source("version", "version.py")
VERSION = "0.3"

setup(
    name="gstmanager",
    #version=gstmanager.VERSION,
    version=VERSION,
    description="gstmanager is a helper for building gstreamer applications",
    author="Florent Thiery",
    author_email="florent.thiery@ubicast.eu",
    url="http://code.google.com/p/gstmanager/",
    license="GNU/LGPLv3",
    packages = ['gstmanager', 'gstmanager/bins',\
                'gstmanager/bins/encoders', \
                'gstmanager/bins/sinks', \
                'gstmanager/bins/srcs', \
                'gstmanager/bins/tees', \
                'gstmanager/detectors', \
                'gstmanager/sbins', \
                'gstmanager/sbins/encoders', \
                'gstmanager/sbins/sinks', \
                'gstmanager/sbins/sources'\
                ],
)
