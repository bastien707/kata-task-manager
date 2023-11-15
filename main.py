class Task:
    def __init__(self, id: int, description: str) -> None:
        self.id = id
        self.checked = False
        self.description = description

    def __str__(self):
        return f"Task(id={self.id}, description={self.description}, checked={self.checked})"

    def check(self):
        self.checked = True
