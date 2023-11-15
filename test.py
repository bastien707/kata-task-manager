import pytest
from main import Task, _update_task_


class TestTask:
    def test_create_task(self) -> None:
        tasklist = []
        task = Task(0, "do something")
        tasklist.append(task)
        assert len(tasklist) == 1

    def test_task_attributes(self) -> None:
        task = Task(0, "do something")
        assert task.description == "do something"
        assert task.checked == False
        assert task.id == 0

    def test_task_check(self) -> None:
        task = Task(0, "do something")
        if task.checked == False:
            task.check()
        assert task.checked == True

    def test_update_task(self) -> None:
        taskList = [Task(0, "do something"), Task(1, "do something else")]
        assert taskList[0].checked == False
        _update_task_(0, taskList)
        assert taskList[0].checked == True
