class ValidadorParentesis:
    def __init__(self):
        self.pila = []

    def esBalanceado(self, expresion):
        for caracter in expresion:
            if caracter == '(':
                self.pila.append(caracter)
            elif caracter == ')':
                if not self.pila:
                    return False
                self.pila.pop()
        return len(self.pila) == 0


if __name__ == "__main__":
    validador = ValidadorParentesis()
    while True:
        expresion = input("Ingresa una expresión matemática (o escribe 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            break
        if validador.esBalanceado(expresion):
            print("La expresión tiene paréntesis balanceados.")
        else:
            print("La expresión NO tiene paréntesis balanceados.")