import pytest
from main import Task


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

    def test_task_str(self) -> None:
        task = Task(0, "do something")
        assert str(task) == "Task(id=0, description=do something, checked=False)"

    def test_task_check(self) -> None:
        task = Task(0, "do something")
        if task.checked == False:
            task.check()
        assert task.checked == True
