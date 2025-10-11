import time
from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, name):
        self._name = name
        self._status = "pending"

    def get_name(self):
        return self._name

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
        
    @abstractmethod
    def execute(self):
        pass

class ReminderTask(Task):
    def __init__(self, name, reminder_time):
        super().__init__(name)
        self.reminder_time = reminder_time

    def execute(self):
        print(f"Reminder set for {self.reminder_time} -> {self.get_name()}")
        self._status = "Completed"

class BackupTask(Task):
    def __init__(self, name, filename):
        super().__init__(name)
        self.filename = filename

    def execute(self):
        print(f"Backing up file: {self.filename}")
        time.sleep(2)
        print(f"Backup complete: {self.filename}")
        self._status = "Completed"


class ComputationTask(Task):
    def __init__(self, name, num=5):
        super().__init__(name)
        self.num = num

    def execute(self):
        result = 1
        for i in range(1, self.num + 1):
            result *= i
        print(f"Calculated factorial of {self.num} = {result}")
        self._status = "Completed"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.log = []

    def add_task(self, task):       
        self.tasks.append(task)

    def run_all(self):
        for task in self.tasks:
            log_entry = f"🔹 Starting task: {task._name} ..."
            self.log.append(log_entry)
            time.sleep(1)
            task.execute()
            self.log.append(f"✅ {task._name} completed successfully!\n")

    def show_status(self):
        print("\n==============Status==============")
        for task in self.tasks:
            print(f"Task name: {task.get_name()}")
            print(f"Status: {task.get_status()}")
        print("==================================")

class AI_System:
    def __init__(self):
        self.manager = TaskManager()

    def run_system(self):
        print("\n-----[AI System Booting...]-----")
        print("\n================================")
        self.manager.run_all()
        print("================================")
        self.manager.show_status()
        


if __name__ == "__main__":
    ai = AI_System()
    ai.manager.add_task(ReminderTask("Study AI", "6 PM"))
    ai.manager.add_task(BackupTask("Backup Photos", "photos.zip"))
    ai.manager.add_task(ComputationTask("Calculate Factorial", num=5))
    ai.run_system()
    
