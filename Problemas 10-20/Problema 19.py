class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"
    
    def tamano(self):
        return len(self.items)
    
class Cola:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return "La cola está vacía"
    
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return "La cola está vacía"
    
    def tamano(self):
        return len(self.items)
    
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def eliminar_al_inicio(self):
        if not self.esta_vacia():
            self.cabeza = self.cabeza.siguiente
        else:
            return "La lista está vacía"
    
    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

def main():
    cola = Cola()
    cola.enqueue(10)
    cola.enqueue(20)
    print(cola.dequeue())  
    print(cola.ver_frente())  

    pila = Pila()
    pila.push(10)
    pila.push(20)
    print(pila.pop())  
    print(pila.ver_tope())  

    lista = ListaEnlazada()
    lista.insertar_al_final(10)
    lista.insertar_al_final(20)
    lista.insertar_al_final(30)
    lista.imprimir_lista()  
    lista.eliminar_al_inicio()
    lista.imprimir_lista()  

main()