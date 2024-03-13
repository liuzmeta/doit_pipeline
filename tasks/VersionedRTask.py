from tasks.Rtask import Rtask
from pathlib import Path

import time
class VersionedRTask(Rtask):
    def setOutputs(self, outputs: list):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        versionedOutputs = []
        for output in outputs:
            p = Path(output)
            versionedOutputs.append(p.parent / f'{timestr}-{p.name}')
        return super().setOutputs(versionedOutputs)