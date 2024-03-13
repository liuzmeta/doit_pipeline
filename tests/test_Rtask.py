import unittest
from tasks.Rtask import Rtask

class TestRtask(unittest.TestCase):
    def test_base(self):
        task = Rtask(openLog=False)
    