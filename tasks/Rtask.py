from tasks.Utils import Utils


class Rtask:
    def __init__(self, name = None, openLog = True) -> None:
        self.name = name
        self.utils = Utils(openLog)
        self.inputs = []
        self.outputs = []
        self.extraParam = []

    def setScript(self, script):
        self.script = self.utils.toAbsPath(script)
        if not self.script.exists():
            raise ValueError(f'Rscript {self.script} does not Exist.')
        if self.name == None:
            self.name = self.script.stem
        return self

    def setInputs(self, inputs: list):
        self.inputs = []
        for input in inputs:
            if isinstance(input, Rtask):
                self.inputs += input.outputs
            else:
                self.inputs.append(self.utils.toAbsPath(input))
        return self

    def setOutputs(self, outputs: list):
        self.outputs = []
        for output in outputs:
            self.outputs.append(self.utils.toAbsPath(output))
        return self
    
    def setExtraParam(self, params, paramOrder: list = []):
        self.extraParam = []
        if isinstance(params, dict):
            for k in paramOrder:
                self.extraParam.append(params.get[k, ''])
        else:
            self.extraParam = params
        return self


    def build(self):
        taskDic = {'basename': self.name, 'verbosity': 2}
        taskDic['actions'] = [(self.utils.execute, ['Rscript', self.script, *self.inputs, *self.outputs, *self.extraParam])]
        taskDic['targets'] = self.outputs
        taskDic['file_dep'] = [self.script, *self.inputs]
        # print(taskDic)

        self.create_doit_tasks = lambda: taskDic
        return self
