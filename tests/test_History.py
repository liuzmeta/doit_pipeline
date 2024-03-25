from pathlib import Path
import tempfile
from tasks.Rtask import RtaskBuilder
from tasks.History import HistoryHanlder
import unittest

from tasks.Utils import Utils

class TestHistory(unittest.TestCase):
    def test_base(self):
        temp_dir = Path(str(tempfile.TemporaryDirectory().name)).parent

        t1 = RtaskBuilder(name='task1', openLog=False) \
            .setScript('R/test1in1out.R') \
            .setInputs(['data/testInput.txt']) \
            .setOutputs(['res/input2']).build()
        hh = HistoryHanlder(temp_dir / 'history')
        u = Utils(False)
        u.executeRtask(t1)
        hh.putHistory(t1, u.process)