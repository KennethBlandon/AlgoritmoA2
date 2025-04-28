class Tasks:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
    def __str__(self):
        return f"Nombre => {self.name}, Descripcion => {self.description}, Prioridad => {self.priority} "

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]
    
    

