import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from task_manager import TaskManager, Task


class TaskManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()
        self.title("Управление на задачи")
        self.create_widgets()

    def refresh_task_list(self):
        self.text_widget.delete('1.0', tk.END)
        for task in self.task_manager.list_tasks():
            self.text_widget.insert(tk.END, f"{task}\n")

    def add_task(self):
        description = simpledialog.askstring("Въведете задача", "Описание на задача:")
        if description:
            self.task_manager.add_task(Task(description))
            self.refresh_task_list()

    def remove_task(self):
        task_index = simpledialog.askinteger("Изтрий задача", "Номер на задачата за изтриване:") - 1
        if 0 <= task_index < len(self.task_manager.tasks):
            self.task_manager.remove_task(task_index)
            self.refresh_task_list()
        else:
            messagebox.showerror("Грешка", "Невалиден индекс на задачата.")

    def save_tasks(self):
        file_path = simpledialog.askstring("Запази задачите", "Име на файла за запазване:")
        if file_path:
            self.task_manager.save_tasks_to_file(file_path)

    def load_tasks(self):
        file_path = simpledialog.askstring("Зареди задачите", "Име на файла за зареждане:")
        if file_path:
            self.task_manager.load_tasks_from_file(file_path)
            self.refresh_task_list()

    def create_widgets(self):
        self.text_widget = scrolledtext.ScrolledText(self, height=10, width=50)
        self.text_widget.pack()

        add_button = tk.Button(self, text="Добави задача", command=self.add_task)
        add_button.pack(fill=tk.X)

        remove_button = tk.Button(self, text="Изтрий задача", command=self.remove_task)
        remove_button.pack(fill=tk.X)

        save_button = tk.Button(self, text="Запази задачите във файл", command=self.save_tasks)
        save_button.pack(fill=tk.X)

        load_button = tk.Button(self, text="Зареди задачите от файл", command=self.load_tasks)
        load_button.pack(fill=tk.X)
