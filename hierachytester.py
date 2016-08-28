__author__ = 'Adam.Dicken'

import unittest
import hierachysolver

class TestHierachySolver(unittest.TestCase):

    def test(self):
        common_manager = hierachysolver.get_common_manager('testcase1')
        print common_manager
