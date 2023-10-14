import os
from sys import platform

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


WORKLOADS_DIR = os.path.join(os.path.dirname(__file__), "..", "workloads")

def get_workloads():
    enabled = []
    for workload in os.listdir(WORKLOADS_DIR):
        if os.path.isdir(os.path.join(WORKLOADS_DIR, workload)):
            w = Workload(workload)
            if w.enabled:
                enabled.append(w)
    return enabled

class Workload:
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(WORKLOADS_DIR, name)
        self._data = None

        self._load()
        
    
    def _load(self):
        path_config = os.path.join(self.path, "config.yml")
        if not os.path.exists(path_config):
            return
        with open(path_config, 'r') as f:
            self._data = load(f, Loader=Loader)

    @property
    def enabled(self):
        if self._data is None:
            return False
        return self._data.get("enabled", False)

    @property
    def command(self):
        if self._data is None:
            return None
        cmd = None

        if platform == "linux" or platform == "linux2":
            cmd = self._data.get("linux-cmd", None)
        elif platform == "darwin":
            cmd = self._data.get("macos-cmd", None)
        elif platform == "win32":
            cmd = self._data.get("windows-cmd", None)
        
        for var in self._data.get("variables", []):
            cmd = cmd.replace(f"${var}", str(self._data["variables"][var]))
        return cmd