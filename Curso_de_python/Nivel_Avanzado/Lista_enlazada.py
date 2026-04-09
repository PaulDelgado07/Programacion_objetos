# class Node: 
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None

# class ListaEnlazada:
#     def __init__(self):
#         self.cabeza = None
    
#     def insertar_nodo(self, dato):
#         nuevo = Node(dato)
#         nuevo.siguiente = self.cabeza
#         self.cabeza = nuevo
    
#     def insertar_final(self, dato): 
#         nuevo = Node(dato)
#         if not self.cabeza:
#             self.cabeza = nuevo
#             return 
        
#         actual = self.cabeza
#         while actual.siguiente: 
#             actual = actual.siguiente
        
#         actual.siguiente = nuevo
        
#     def recorrer_lista(self):
#         actual = self.cabeza
#         while actual:
#             print(actual.dato)
#             actual = actual.siguiente

        
# ls = ListaEnlazada()
# ls.insertar_nodo(10)
# ls.insertar_nodo(20)
# ls.insertar_nodo(30)
# ls.insertar_nodo(40)
# ls.insertar_final(0)
# ls.recorrer_lista()

class Node:
    def __init__(self, dato):
        self.dato = dato 
        self.siguiente = None 

class ListaEnlazada: 
    def __init__(self):
        self.cabecera = None 
    
    def insertar_inicio(self, dato): 
        nuevo = Node(dato)
        nuevo.siguiente = self.cabecera 
        self.cabecera = nuevo 
    
    def insertar_final(self, dato):
        nuevo = Node(dato)
        #verificar si la lista está vacia 
        if self.cabecera is None:
            self.cabecera = nuevo
            return
        
        #Si es que no esta vacia
        aux = self.cabecera 
        while aux.siguiente:
            aux = aux.siguiente
        
        aux.siguiente = nuevo 

    def mostrar_lista(self):
        aux = self.cabecera 
        while aux:
            print(aux.dato, end=" -> ")
            aux = aux.siguiente
        print("None")

ls = ListaEnlazada()
ls.insertar_inicio(10)
ls.insertar_inicio(20)
ls.insertar_inicio(30)
ls.insertar_inicio(40)
ls.insertar_final(50)
ls.mostrar_lista()
