from pathlib import Path
from subprocess import run
import os

class Utils:
    def __init__(self, logSwitch = True) -> None:
        self.logSwitch = logSwitch

        self.utilPath = Path(__file__)
        self.taskRoot = self.utilPath.parent.parent
        self.rRoot = self.taskRoot / 'R'
        self.meta = self.taskRoot / '.meta'
        self.tmp = self.taskRoot / 'tmp'

        self.tmp.mkdir(parents=True, exist_ok=True)

    def toAbsPath(self, pathStr) -> Path:
        path = Path(pathStr)
        if path.is_absolute(): 
            return path
        else:
            return self.taskRoot / pathStr
        
    def execute(self, *args):
        if os.name == 'nt':
            if cmd[0] == 'Rscript':
                cmd = [cmd[0]] + ["--max-mem-size=20000M"] + cmd[1:]
        cmd = [str(i) for i in args]
        p = run(cmd, capture_output=True)
        print('\n')
        print(f'executing cmd: {cmd}')
        print('\n')
        print(p.stdout)
        print(p.stderr)
        print('\n')


    