from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

def test_suite():
    """Returns unittest.TestSuite of desisim tests for use by setup.py"""
    from os.path import dirname
    surveysim_dir = dirname(dirname(__file__))
    print(desisim_dir)
    return unittest.defaultTestLoader.discover(surveysim_dir,
        top_level_dir=dirname(surveysim_dir))
