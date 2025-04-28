# Construye una pequeña aplicación para gestionar tareas pendientes utilizando pilas. Primero, crea una clase Tarea con los atributos nombre, descripcion y prioridad. Luego, desarrolla una clase PilaTareas que permita almacenar tareas mediante un método push, eliminar la tarea más reciente con pop y consultar la tarea actual utilizando peek. Finalmente, en la clase Main, crea un programa que permita agregar tres tareas diferentes y luego procesarlas una a una, mostrando los detalles de cada tarea a medida que son eliminadas de la pila.
from controllers import dao
from models import classes
dao1 = dao.TasksHandler()
def main():
    while True:
        print("1. Agregar tarea")
        print("2. Finalizar última tarea")
        print("3. Consultar Tarea actual")
        
        user_input = int(input("=> "))
        
        match user_input:
            case 1:
                name = input("nombre => ")
                description = input("descripción => ")
                priority = input("prioridad => ")
                task = classes.Tasks(name, description, priority)
                dao1.add_task(task)
            case 2:
                print("Tarea finalizada: ", dao1.current_task())
                dao1.end_task()
            case 3:
                print(dao1.current_task())

main()