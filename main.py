taskList = []
task_id = 0  # Global counter for task IDs


class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.checked = False

    def __str__(self):
        checked_str = '[' + str("x") + \
            ']' if self.checked == True else '[ ]'
        return str(self.id) + ' ' + checked_str + ' ' + self.description

    def check(self):
        self.checked = True


def task_runner():
    global task_id  # Declare task_id as global so we can modify it
    menu = True

    while menu:
        if taskList == []:
            print("No tasks yet")
        else:
            for task in taskList:
                print(task)

        operator_input = input("Quelle action voulez-vous effectuer ? " + "\n")
        operator, _, user_input = operator_input.partition(' ')

        if operator == "+":
            task_id += 1  # Increment task_id
            _add_task_(task_id, user_input)  # Pass task_id to _add_task_
        elif operator == "x":
            _update_task_(int(user_input), taskList)
        elif operator == "q":
            menu = False
            print("Bye bye")


def _add_task_(id: int, description: str) -> Task:
    if description == "":
        print("Need to add a description, please add one")
    else:
        taskList.append(Task(id, description))  # Pass id to Task


def _update_task_(id: int, taskList: list) -> None:
    for task in taskList:
        if task.id == id:
            task.check()


task_runner()
