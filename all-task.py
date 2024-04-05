
# Задача: Создать класс Task, который позволяет управлять задачами.
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Требуется реализовать функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных)
# задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "не выполнено"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Задача добавлена")

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Задача удалена")
        else:
            print("Задачи с таким номером не существует")

    def set_task_deadline(self, task_index, new_deadline):
        if task_index < len(self.tasks):
            self.tasks[task_index].deadline = new_deadline
            print("Срок выполнения задачи обновлен")
        else:
            print("Задачи с таким номером не существует")

    def mark_task_as_done(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index].status = "выполнено"
            print("Задача отмечена как выполненная")
        else:
            print("Задачи с таким номером не существует")

    def mark_task_as_undone(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index].status = "не выполнено"
            print("Статус задачи изменен на 'не выполнено'")
        else:
            print("Задачи с таким номером не существует")

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "не выполнено"]
        if current_tasks:
            for index, task in enumerate(current_tasks):
                print(f"{index + 1}. {task.description} (до {task.deadline})")
        else:
            print("Нет текущих задач")

    def get_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.status == "выполнено"]
        if completed_tasks:
            for index, task in enumerate(completed_tasks):
                print(f"{index + 1}. {task.description} (выполнено)")
        else:
            print("Нет выполненных задач")

task_manager = TaskManager()
while True:
    print("\n1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Установить срок выполнения задачи")
    print("4. Отметить задачу как выполненную")
    print("5. Отметить задачу как невыполненную")
    print("6. Вывести список текущих задач")
    print("7. Вывести список выполненных задач")
    print("8. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        new_task = Task(description, deadline)
        task_manager.add_task(new_task)
    elif choice == "2":
        index = int(input("Введите номер задачи для удаления: ")) - 1
        task_manager.remove_task(index)
    elif choice == "3":
        index = int(input("Введите номер задачи для обновления срока выполнения: ")) - 1
        new_deadline = input("Введите новый срок выполнения: ")
        task_manager.set_task_deadline(index, new_deadline)
    elif choice == "4":
        index = int(input("Введите номер выполненной задачи: ")) - 1
        task_manager.mark_task_as_done(index)
    elif choice == "5":
        index = int(input("Введите номер невыполненной задачи: ")) - 1
        task_manager.mark_task_as_undone(index)
    elif choice == "6":
        task_manager.get_current_tasks()
    elif choice == "7":
        task_manager.get_completed_tasks()
    elif choice == "8":
        break
    else:
        print("Некорректный выбор")