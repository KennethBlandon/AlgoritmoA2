from models import classes
class TasksHandler:
    def __init__(self):
        self.tasks = classes.Stack()
    
    def add_task(self, task):
        self.tasks.push(task)
    
    def end_task(self):
        self.tasks.pop()
    
    def current_task(self):
        return self.tasks.peek()
    