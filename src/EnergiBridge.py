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
        return [program_path, "-i", str(self.settings.interval), "-o", f"{task.output_path}.csv", "--command-output", f"{task.output_path}.log"]

    def run(self, task: src.runner.Task):
        os.makedirs(os.path.dirname(task.output_path), exist_ok=True)
        subprocess.Popen(" ".join(self.cmd(task) + ['--', task.workload.command]), shell=True).wait()