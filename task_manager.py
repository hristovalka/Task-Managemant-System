class Task:
    def __init__(self, description, status='Неизпълнена'):
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.description} - {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def update_task(self, task_index, description=None, status=None):
        if 0 <= task_index < len(self.tasks):
            if description:
                self.tasks[task_index].description = description
            if status:
                self.tasks[task_index].status = status

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def save_tasks_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.description},{task.status}\n")
        except IOError as e:
            print(f"Error saving tasks to file: {e}")

    def load_tasks_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.tasks = [Task(*line.strip().split(',')) for line in file]
        except IOError as e:
            print(f"Error loading tasks from file: {e}")

