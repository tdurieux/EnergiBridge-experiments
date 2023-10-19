from __future__ import annotations

import subprocess, os, sys, datetime, json

import src.runner

class EnergiBridge:
    def __init__(self, settings) -> None:
        self.settings = settings
        pass

    def cmd(self, task: src.runner.Task):
        program_path = os.path.join(os.path.dirname(__file__), "..", "energibridge", "energibridge")
        if sys.platform == "win32":
            program_path += ".exe"
        return [program_path, "-i", str(self.settings.interval), "--max-execution", str(task.workload.max_execution), "-o", f"{task.output_path}.csv", "--command-output", f"{task.output_path}.log"]

    def run(self, task: src.runner.Task):
        start = datetime.datetime.now()
        
        os.makedirs(os.path.dirname(task.output_path), exist_ok=True)
        o = {
            "startingTime": start.isoformat(),
            "energiBridgeCmd": " ".join(self.cmd(task)),
            "taskCmd": task.workload.command,
        }
        try:
            subprocess.Popen(" ".join(self.cmd(task) + ['--', task.workload.command]), shell=True).wait()
        finally:
            print(f"[TASK {task.workload.name} - {task.id}] DONE in {datetime.datetime.now() - start}")
            o["endingTime"] = datetime.datetime.now().isoformat()
            with open(f"{task.output_path}.json", "w") as f:
                json.dump(o, f, indent=4)