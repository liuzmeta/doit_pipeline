from pathlib import Path
import json
import datetime

class History:
    def __init__(self, rtask, process) -> None:
        self.id = datetime.datetime.now()
        self.script = rtask.script
        self.input = rtask.inputs
        self.params = rtask.extraParam
        if process.returncode == 0:
            self.target = rtask.outputs
            self.status = 'SUCCESS'
            self.message = ''
        else:
            self.target = None
            self.status = 'ERROR'
            self.message = process.stderr

    def ser(self):
        res = {}
        for k in self.__dict__:
            v = self.__dict__[k]
            if isinstance(v, list):
                res[k] = [str(i) for i in v]
            else:
                res[k] = str(v)
        return res


class HistoryHanlder:
    def __init__(self, historyPath) -> None:
        self.historyPath = Path(historyPath)

    def loadHistory(self):
        try:
            self.f = open(self.historyPath, 'r')
            self.allHistory = json.load(self.f)
        except:
            self.historyPath.parent.mkdir(parents=True, exist_ok=True)
            self.allHistory = []
        self.f = open(self.historyPath, 'w')
        

    def putHistory(self, task, process):
        self.loadHistory()
        history = History(task, process)
        self.allHistory.append(history.ser())
        json.dump(self.allHistory ,self.f, indent=4)
        self.f.close()
    