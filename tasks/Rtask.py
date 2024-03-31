from tasks.Utils import Utils
from pathlib import Path
import time

class Rtask:
    def __init__(self, name) -> None:
        self.name = name
        self.script = None
        self.inputs = []
        self.outputs = []
        self.extraParam = []


class RtaskBuilder:
    def __init__(self, name = None, openLog = True) -> None:
        self.rtask = Rtask(name)
        self.utils = Utils(openLog)
        self.inputs = []
        self.outputs = []
        self.extraParam = []

    def setScript(self, script):
        _script = self.utils.toAbsPath(script)
        if not _script.exists():
            raise ValueError(f'Rscript {_script} does not Exist.')
        self.rtask.script = _script
        if self.rtask.name == None:
            self.rtask.name = _script.stem
        return self

    def setInputs(self, inputs: list):
        _inputs = []
        for input in inputs:
            if isinstance(input, Rtask):
                _inputs += input.outputs
            else:
                _inputs.append(self.utils.toAbsPath(input))
        self.rtask.inputs = _inputs
        return self

    def setOutputs(self, outputs: list):
        _outputs = []
        for output in outputs:
            _output = self.utils.toAbsPath(output)
            _output.parent.mkdir(parents=True, exist_ok=True)
            _outputs.append(_output)
        self.rtask.outputs = _outputs
        return self
    
    def setVersionedOutputs(self, outputs: list):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        versionedOutputs = []
        for output in outputs:
            p = Path(output)
            versionedOutputs.append(p.parent / f'{timestr}-{p.name}')
        self.rtask.outputs = versionedOutputs
        return self
    
    def setExtraParam(self, params, paramOrder: list = []):
        _extraParam = []
        if isinstance(params, dict):
            for k in paramOrder:
                _extraParam.append(params.get[k, ''])
        else:
            _extraParam = params
        self.rtask.extraParam = _extraParam
        return self

    def build(self):
        taskDic = {'basename': self.rtask.name, 'verbosity': 2}
        taskDic['actions'] = [(self.utils.executeRtask, [self.rtask])]
        taskDic['targets'] = self.rtask.outputs
        taskDic['file_dep'] = [self.rtask.script, *self.rtask.inputs]
        # print(taskDic)

        self.rtask.create_doit_tasks = lambda: taskDic
        return self.rtask
