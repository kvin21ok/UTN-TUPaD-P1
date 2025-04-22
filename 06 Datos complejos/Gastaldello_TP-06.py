'''
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
'''
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print(precios_frutas)

################################################################

'''
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
'''
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
print(precios_frutas)

####################################################################

'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
'''
lista_sin_precios = list(precios_frutas.keys())
print(lista_sin_precios)

##################################################################

'''
4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
años."
'''
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    
    def saludar(self):
        print(f'¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.')

persona1 = Persona('Ivanka', 'Rusia', 33)
persona1.saludar()

######################################################################

'''
5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
'''
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return(math.pi * (self.radio ** 2))
    
    def calcular_perimetro(self):
        return(2 * math.pi * self.radio)
    
circulo1 = Circulo(3)
print(f'Area del circulo: {circulo1.calcular_area()}')
print(f'Perimetro del circulo: {circulo1.calcular_perimetro()}')

#####################################################################

'''
#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
#balanceados usando una pila.
'''
class Pila:
    def __init__(self):
        self.elementos = []
    
    def push(self, valor):
        self.elementos.append(valor)

    def pop(self):
        return self.elementos.pop() if not self.es_vacia() else 'Pila vacia'
    
    def es_vacia(self):
        return len(self.elementos) == 0
    
    def ver_tope(self):
        return self.elementos(-1) if not self.es_vacia() else 'Pila vacia'

class Balanceo:
    def __init__(self):
        self.pila = Pila()

    def verificar_balanceo(self, cadena):
        parejas = {')': '(', '}': '{', ']': '['}

        for caracter in cadena:
            if caracter in parejas.values():
                self.pila.push(caracter)
            elif caracter in parejas:
                if not self.pila.es_vacia() and self.pila.pop() == parejas[caracter]:
                    continue
                else:
                    return False
        return self.pila.es_vacia()

balanceador = Balanceo()

pila1 = '({[]})'
print(balanceador.verificar_balanceo(pila1))

pila2 = '({]})'
print(balanceador.verificar_balanceo(pila2))

#######################################################################

'''
7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila.
'''
from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar (self, elemento):
        self.elementos.append(elemento)

    def desencolar (self):
        return self.elementos.popleft() if not self.esta_vacia() else 'Cola vacia'
    
    def esta_vacia (self):
        return len(self.elementos) == 0
    
    def ver_frente (self):
        return self.elementos[0] if not self.esta_vacia() else 'Cola vacia'
    
cola_banco = Cola()
cola_banco.encolar('1')
cola_banco.encolar('2')
cola_banco.encolar('3')
cola_banco.encolar('4')
cola_banco.desencolar()
cola_banco.desencolar()
print('Proximo en cola: ')
print(cola_banco.ver_frente())

#############################################################################

'''
8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
los valores almacenados.
'''
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar (self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar (self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end = ' => ')
            actual = actual.siguiente
        print('None')

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(4)
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
print('Lista enlazada: ')
lista.mostrar()

###################################################################

'''
9) Dada una lista enlazada, implementa una función para invertirla.
'''
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar (self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar (self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end = ' => ')
            actual = actual.siguiente
        print('None')
    
    def invertir (self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
            self.cabeza = anterior

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(4)
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
print('Lista original: ')
lista.mostrar()
lista.invertir()
print('Lista invertida: ')
lista.mostrar()