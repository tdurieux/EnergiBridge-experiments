from __future__ import annotations

import subprocess, os, sys

import src.runner

class EnergiBridge:
    def __init__(self, settings) -> None:
        self.settings = settings
        pass

    def cmd(self, task: src.runner.Task):
        program_path = os.path.join(os.path.dirname(__file__), "..", "energibridge", "energi_bridge")
        if sys.platform == "win32":
            program_path += ".exe"
        output_path = os.path.join(self.settings.output, str(task.id))
        return f"{program_path} -i {self.settings.interval} -o {output_path}.csv --command-output {output_path}.log"

    def run(self, task: src.runner.Task):
        cmd = self.cmd(task) + " -- " + task.workload.command
        os.makedirs(self.settings.output, exist_ok=True)
        subprocess.run(cmd, shell=True, check=True)