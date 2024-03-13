from tasks.VersionedRTask import VersionedRTask
from tasks.Rtask import Rtask

t1 = Rtask(name='task1', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs(['data/testInput.txt']) \
    .setOutputs(['input2']).build()

t2 = Rtask(name='task2', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs([t1]) \
    .setOutputs(['input3']).build()

t3 = VersionedRTask(name='task3', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs([t1]) \
    .setOutputs(['input3']).build()


t4 = Rtask(name='task4', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs([t3]) \
    .setOutputs(['input4']).build()