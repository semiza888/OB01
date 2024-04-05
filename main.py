# Задача: Создать класс Task, который позволяет управлять задачами.
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Требуется реализовать функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных)
# задач.

class Task:
    def __init__(self, description, due_date, status='not_done'):
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_done(self):
        self.status = 'done'

def add_task(tasks, description, due_date):
    tasks.append(Task(description, due_date))

def mark_done_tasks(tasks, index):
    tasks[index].mark_done()

def print_current_tasks(tasks):
    current_tasks = [task for task in tasks if task.status == 'not_done']
    for i, task in enumerate(current_tasks):
        print(f'{i+1}. {task.description} (до: {task.due_date})')

tasks = []

while True:
    print("\nВыберите действие:")
    print("1. Добавить задачу")
    print("2. Отметить задачу выполненной")
    print("3. Удалить задачу")
    print("4. Изменить срок выполнения задачи")
    print("5. Вывести текущую задачу")
    print("6. Вывести все текущие задачи")
    print("7. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        description = input("Введите описание задачи: ")
        due_date = input("Введите срок выполнения (дд.мм.гггг): ")
        add_task(tasks, description, due_date)
    elif choice == '2':
        print_current_tasks(tasks)
        index = int(input("Введите номер задачи для отметки выполненной: ")) - 1
        mark_done_tasks(tasks, index)
    elif choice == '3':
        print_current_tasks(tasks)
        index = int(input("Введите номер задачи для удаления: ")) - 1
        del tasks[index]
    elif choice == '4':
        print_current_tasks(tasks)
        index = int(input("Введите номер задачи для изменения срока исполнения: ")) - 1
        new_due_date = input("Введите новый срок исполнения задачи (дд.мм.гггг): ")
        tasks[index].due_date = new_due_date
    elif choice == '5':
        print_current_tasks(tasks)
        index = int(input("Введите номер задачи для просмотра: ")) - 1
        print(f'{tasks[index].description} (до: {tasks[index].due_date})')
    elif choice == '6':
        print_current_tasks(tasks)
    elif choice == '7':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")