import unittest
from tasks.Utils import Utils

class TestRtask(unittest.TestCase):
    def test_base(self):
        t = Utils()
        self.assertIsNotNone(t.utilPath)
        self.assertIsNotNone(t.taskRoot)
        self.assertIsNotNone(t.rRoot)
        self.assertNotEqual(t.toAbsPath('test'), 'test')

        print(t.utilPath)
        print(t.taskRoot)
        print(t.toAbsPath('test'))