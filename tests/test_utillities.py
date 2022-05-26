
import unittest
import pandas as pd
import numpy as np
import sys
import os
from pprint import pprint
import json
sys.path.append('../')
from scripts.utilities import Utilities



class TestUtilities(unittest.TestCase):


    def test_get_df(self):
        utilities = Utilities()
        train = utilities.get_df(path='data/train.csv',rep='./',rev='tagv1')
        self.assertEqual(len(train), 1017209)
    
    
if __name__ == '__main__':
    unittest.main()