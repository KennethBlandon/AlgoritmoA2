import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def pausa():
    input("Presione Enter para continuar...")

class Stack:
    def __init__(self):
        self.items = []
    
    def esta_vacio(self):
        return len(self.items) == 0
    def push(self , item):
        self.items.append(item)
    def pop(self):
        if not self.esta_vacio():
            return self.items.pop()
        return None
    def peek(self):
        if not self.esta_vacio():
            return self.items[-1]
        return None
    def down(self):
        if not self.esta_vacio():
            return self.items[0]
        return None
    def size(self):
        return len(self.items)
    def mostrar(self):
        if not self.esta_vacio():
            print("Contenido de la pila:")
            for item in reversed(self.items):
                print(item)
        else:
            print("La pila está vacía.")

pila = Stack()

class HistorialNavegador:
    def __init__(self):
        self.historial = Stack()
    def visitar_pagina(self, url):
        self.historial.push(url)
        print(f"Visitando página: {url}")
    def pagina_actual(self):
        pagina = self.historial.peek()
        if pagina:
            print(f"Página actual: {pagina}")
        else:
            print("No hay páginas en el historial.")
    def volver_pagina_anterior(self):
        pagina = self.historial.pop()
        if pagina:
            print(f"Volviendo de la página: {pagina}")
        else:
            print("No hay páginas anteriores para volver.")
    
    def ver_historial(self):
        if not self.historial.esta_vacio():
            print("Historial de páginas visitadas:")
            self.historial.mostrar()
        else:
            print("El historial está vacío.")

def main():
    navegador = HistorialNavegador()
    while True:
        limpiar_pantalla()
        print("===============================")
        print("     HISTORIAL NAVEGADOR      ")
        print("===============================")
        print("1. Visitar nueva página")
        print("2. Ver página actual")
        print("3. Volver a la página anterior")
        print("4. Ver historial de páginas")
        print("0. Salir")
        print("------------------------------")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            url = input("Ingrese la URL de la página: ")
            navegador.visitar_pagina(url)
            pausa()
        elif opcion == 2:
            navegador.pagina_actual()
            pausa()
        elif opcion == 3:
            navegador.volver_pagina_anterior()
            pausa()
        elif opcion == 4:
            navegador.ver_historial()
            pausa()
        elif opcion == 0:
            print("Saliendo del programa.")
            pausa()
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()