#Desarrolla una clase llamada PilaCaracteres para trabajar exclusivamente con caracteres (char). Implementa los métodos necesarios para agregar caracteres a la pila y eliminarlos. A continuación, crea un método llamado invertirCadena(String texto), que reciba una cadena, la almacene carácter por carácter en la pila, y luego reconstruya la cadena en orden inverso. En la clase Main, solicita al usuario que ingrese una cadena de texto y muestra en pantalla su versión invertida utilizando tu pila.

class PilaCaracteres:
    def __init__(self):
        self.items = []

    def agregar(self, char):
        if len(char) == 1: 
            self.items.append(char)
        else:
            print("Error: Solo se pueden agregar caracteres individuales.") 
    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía, no se puede eliminar.")

    def esta_vacia(self):
        return len(self.items) == 0

    def invertir_cadena(self, texto):
        for char in texto:
            self.agregar(char)
        
        texto_invertido = ""
        while not self.esta_vacia():
            texto_invertido += self.eliminar()
        
        return texto_invertido


if __name__ == "__main__":
    pila = PilaCaracteres()
    
    texto = input("Ingrese una cadena de texto: ")
    texto_invertido = pila.invertir_cadena(texto)
  
    print("\nResultados:")
    print("======================================================================================================================================================================")
    print(f"Texto original: {texto}")   
    print(f"Texto invertido: {texto_invertido}")
    print("======================================================================================================================================================================")