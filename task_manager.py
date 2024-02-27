class Task:
    """Клас, който представлява индивидуална задача с описание и статус."""

    def __init__(self, description, status='Неизпълнена'):
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.description} - {self.status}"


class TaskManager:
    """Клас, който управлява колекция от задачи."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Задачата беше успешно добавена.")

    def list_tasks(self):
        if not self.tasks:
            print("Няма създадени задачи.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def update_task(self, task_index, description=None, status=None):
        if 0 <= task_index < len(self.tasks):
            if description:
                self.tasks[task_index].description = description
            if status:
                self.tasks[task_index].status = status
            print("Задачата беше успешно актуализирана.")
        else:
            print("Грешка: Невалиден индекс на задачата.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Задачата беше успешно изтрита.")
        else:
            print("Грешка: Невалиден индекс на задачата.")

    def save_tasks_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.description},{task.status}\\n")
            print(f"Задачите бяха успешно запазени в {file_path}.")
        except IOError:
            print("Грешка: Неуспешно запазване на файла.")

    def load_tasks_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.tasks = [Task(*line.strip().split(',')) for line in file]
            print(f"Задачите бяха успешно заредени от {file_path}.")
        except IOError:
            print("Грешка: Неуспешно зареждане на файла.")
        except ValueError:
            print("Грешка: Неправилен формат на данните във файла.")


def add_task_ui(task_manager):
    description = input("Описание на задачата: ").strip()
    if description:
        task_manager.add_task(Task(description))
    else:
        print("Описанието не може да бъде празно.")


def get_task_index():
    try:
        task_index = int(input("Въведете номер на задачата: ")) - 1
        return task_index
    except ValueError:
        print("Грешка: Въведете валиден номер.")
        return None


def update_task_ui(task_manager):
    task_index = get_task_index()
    if task_index is None: return
    description = input("Ново описание (натиснете Enter за пропускане): ").strip()
    status = input("Нов статус (натиснете Enter за пропускане): ").strip()
    task_manager.update_task(task_index, description or None, status or None)


def remove_task_ui(task_manager):
    task_index = get_task_index()
    if task_index is None: return
    task_manager.remove_task(task_index)


def save_tasks_ui(task_manager):
    file_path = input("Име на файла за запазване: ").strip()
    if file_path:
        task_manager.save_tasks_to_file(file_path)
    else:
        print("Името на файла не може да бъде празно.")


def load_tasks_ui(task_manager):
    file_path = input("Име на файла за зареждане: ").strip()
    if file_path:
        task_manager.load_tasks_from_file(file_path)
    else:
        print("Името на файла не може да бъде празно.")


def main_menu():
    task_manager = TaskManager()
    while True:
        print("1. Добавяне на задача")
        print("2. Преглед на всички задачи")
        print("3. Редактиране на задача")
        print("4. Изтриване на задача")
        print("5. Запазване на задачите във файл")
        print("6. Зареждане на задачите от файл")
        print("7. Изход")
        choice = input("Изберете опция: ")

        if choice == '1':
            add_task_ui(task_manager)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            update_task_ui(task_manager)
        elif choice == '4':
            remove_task_ui(task_manager)
        elif choice == '5':
            save_tasks_ui(task_manager)
        elif choice == '6':
            load_tasks_ui(task_manager)
        elif choice == '7':
            break
        else:
            print("Невалидна опция, моля опитайте отново.")


if __name__ == "__main__":
    main_menu()
