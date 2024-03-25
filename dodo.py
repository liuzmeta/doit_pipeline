from tasks.Rtask import RtaskBuilder

sc_rna_for_all = RtaskBuilder(name='task1', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs(['data/testInput.txt']) \
    .setOutputs(['res/input2']).build()

t2 = RtaskBuilder(name='task2', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs([sc_rna_for_all]) \
    .setOutputs(['res/input3']).build()

t3 = RtaskBuilder(name='task3', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs([sc_rna_for_all]) \
    .setVersionedOutputs(['res/input3']).build()


t4 = RtaskBuilder(name='task4', openLog=False) \
    .setScript('R/test1in1out.R') \
    .setInputs([t3]) \
    .setOutputs(['res/input4']).build()