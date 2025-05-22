'''
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return(num * factorial(num-1))

numero = int(input('Ingrese un numero para calcular el factorial de todos los numeros entre el 1 el ingresado: '))
for i in range(1, numero + 1):
    print(f'{i}! = {factorial(i)}')

##################################################################################

'''
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)

numero = int(input('Ingrese un numero para mostrar la serie completa de fibonacci hasta la posicion del numero ingresado: '))
for i in range(numero + 1):
    print(fibonacci(i))

##################################################################################

'''
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n**m = n * n**(𝑚-1)
. Prueba esta función en un algoritmo general.
'''
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

numero1 = int(input('Ingrese una base: '))
numero2 = int(input('Ingrese un exponente: '))
print(f'La potencia de {numero1} elevado a {numero2} es {potencia(numero1, numero2)}')

####################################################################################

'''
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
'''
def conversion_a_binario(decimal):
    if decimal < 2: #de esta manera puedo manejar en una sola linea si el numero ingrresado es 0 o 1
        return str(decimal)
    else:
        return conversion_a_binario(decimal // 2) + str(decimal % 2)

numero = int(input('Ingrese un numero positivo a convertir en binario: '))
print(f'{numero} convertido a binario es = {conversion_a_binario(numero)}')

###################################################################################

'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''
def chau_espacios_y_tildes(texto):
    reemplazos = {
        'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',
        'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U',
    }
    texto = texto.replace(' ', '')
    for original, reemplazo in reemplazos.items(): #recorre el diccionario
        texto = texto.replace(original, reemplazo) #reemplaza la vocal tildada por su forma sin tildar
    return texto

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

frase = input('Ingrese palabra o frase para saber si es palindromo: ')
frase_filtrada = chau_espacios_y_tildes(frase)
print(es_palindromo(frase_filtrada))

################################################################################################

'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
'''
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input('Ingrese un numero para sumarle sus cifras: '))
print(f'La suma de las cifras de {numero} es = {suma_digitos(numero)}')

######################################################################################

'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
'''
def contar_bloques(n):
    if n <= 1:
        return n
    else:
        return n + contar_bloques(n - 1)

nivel = int(input('Ingrese el numero de niveles que quiere que tenga la piramide: '))
print(f'Para una piramide de {nivel} niveles es necesario contar con {contar_bloques(nivel)} bloques')

################################################################################################

'''8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
'''
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        contador = 1 if numero % 10 == digito else 0
        return contador + contar_digito(numero // 10, digito)

num = int(input('Ingrese un numero: '))
dig = int(input('Ingrese el digito que quiere contar cuantas veces aparece en el numero ingresado: '))
print(f'El digito {dig} aparece {contar_digito(num, dig)} veces en el numero {num}')