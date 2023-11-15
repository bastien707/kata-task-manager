taskList = []
task_id = 0  # Global counter for task IDs

class Task :
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.checked = False

    def __str__(self):
        checked_str = '[' + str(self.checked) + ']' if self.checked == True else '[ ]'
        return str(self.id) + ' ' + checked_str + ' ' + self.description

def rpn_reader():
    global task_id  # Declare task_id as global so we can modify it
    menu = True

    while menu: 
        if taskList == []:
            print("No tasks yet")
        else:
            for task in taskList:
                print(task)

        operator_input = input("Quelle action voulez-vous effectuer ?")
        operator, _, description = operator_input.partition(' ')

        if operator == "+":
            task_id += 1  # Increment task_id
            _add_task_(task_id, description)  # Pass task_id to _add_task_

def _add_task_(id: int, description: str) -> Task:
    if description == "":
        print("Need to add a description, please add one")
    else:
        taskList.append(Task(id, description))  # Pass id to Task

rpn_reader()