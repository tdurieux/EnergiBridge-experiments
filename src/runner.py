
import random
from src.EnergiBridge import EnergiBridge

from src.Workload import Workload

class Task:
    def __init__(self, id, workload: Workload, settings):
        self.id = id
        self.workload = workload
        self.settings = settings

    def run(self):
        EnergiBridge(self.settings).run(self)

def generate_tasks(workloads: [Workload], settings):
    tasks = []
    row = 0
    for workload in workloads:
        for i in range(settings.iterations):
            tasks.append(Task(i + 1 + (row * settings.iterations), workload, settings))
        row += 1
    tasks.sort(key = lambda x: random.random())
    warmup_workload = Workload("warmup")
    return [Task(-1, warmup_workload, settings)] + tasks

def run(workloads: [Workload], settings):
    tasks = generate_tasks(workloads, settings)
    for task in tasks:
        task.run()