# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input('Ingrese su edad: '))
if edad > 18:
    print('Es mayor de edad')

###########################################################################################

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = float(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado!')
else:
    print('Desaprobado :(')

############################################################################################

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input('Ingrese un numero par por favor: '))

while (numero % 2 != 0):
    print('He dicho un numero par, intente nuevamente')
    numero = int(input('Ingrese un numero par por favor: '))
print('Ha ingresado un numero par!')

##############################################################################################

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input('Ingrese su edad: '))

if edad < 0:
    print('Usted ingresó una edad no válida')
elif edad < 12:
    print('Usted es un/a niño/a')
elif edad < 18:
    print('Usted es un/a adolescente')
elif edad < 30:
    print('Usted es un/a adulto/a joven')
else:
    print('Usted es un/a adulto/a')

######################################################################################################

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contra = input('Ingrese una contraseña de entre 8 y 14 caracteres: ')

if len(contra) >= 8 and len(contra) <= 14:
    print('Ha ingresado una contraseña correcta!')
else:
    print('La cantidad de caracteres para la contraseña es incorrecta')

# NOTA: PODRIA USAR UN WHILE PARA QUE EL PROGRAMA SE SIGA EJECUTANDO HASTA QUE LA CANTIDAD DE CARACTERES SEA LA CORRECTA PERO NO ME LO PIDE EL EJERCICIO

#########################################################################################################

# 6) La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
print(f'Media: {mean(numeros_aleatorios)}, mediana: {median(numeros_aleatorios)}, moda: {mode(numeros_aleatorios)}') #elijo mostrar cada parametro

if mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print('No hay sesgo en la lista de numeros')
elif (mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print('Hay sesgo positivo en la lista de numeros')
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)) and (median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print('Hay sesgo negativo en la lista de numeros')
else:
    print('No hay criterio')

###################################################################################################

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input('Ingrese una palabra o frase: ')

if frase[-1].lower() in 'aeiou': #busco la ultima letra y si es vocal le agrego "!" a la variable que luego se imprime ya sea editada o no segun el caso
    frase += '!'
print(frase)

####################################################################################################

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input('Ingrese su nombre y el numero segun que opcion desee: 1. Si quiere su nombre en mayúsculas / 2. Si quiere su nombre en minúsculas / 3. Si quiere su nombre con la primera letra mayúscula: ')

if nombre[-1] == '1':
    nombre = nombre.upper()
    nombre = nombre[:-1] #aqui elimino el ultimo caracter del string que seria la opcion indicada asi no se muestra luego en pantalla
elif nombre[-1] == '2':
    nombre = nombre.lower()
    nombre = nombre[:-1]
elif nombre[-1] == '3':
    nombre = nombre.title()
    nombre = nombre[:-1]

print(nombre)

#####################################################################################################33

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto = float(input('Ingrese la magnitud del terremoto: '))

if terremoto < 3:
    print('Muy leve (imperceptible)')
elif terremoto < 4:
    print('Leve (ligeramente perceptible)')
elif terremoto < 5:
    print('Moderado (sentido por personas pero inofensivo)')
elif terremoto < 6:
    print('Fuerte (puede causar daños en estructuras debiles)')
elif terremoto < 7:
    print('Muy fuerte (daños significativos)')
elif terremoto >= 7:
    print('Extremo (daños a gran escala)')

##########################################################################################################

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input('Ingrese el hemisferio en el que se encuentra (N/S): ').strip().upper()
mes = input('Ingrese el mes actual (Ejemplo: enero, febrero, etc.): ').strip().lower()
dia = int(input('Ingrese el día del mes: '))

#definio las estaciones según el hemisferio
if hemisferio == 'N':
    if (mes == 'marzo' and dia >= 21) or mes in ['abril', 'mayo'] or (mes == 'junio' and dia < 21):
        estacion = 'Primavera'
    elif (mes == 'junio' and dia >= 21) or mes in ['julio', 'agosto'] or (mes == 'septiembre' and dia < 23):
        estacion = 'Verano'
    elif (mes == 'septiembre' and dia >= 23) or mes in ['octubre', 'noviembre'] or (mes == 'diciembre' and dia < 21):
        estacion = 'Otoño'
    else:
        estacion = 'Invierno'
elif hemisferio == 'S':
    if (mes == 'marzo' and dia >= 21) or mes in ['abril', 'mayo'] or (mes == 'junio' and dia < 21):
        estacion = 'Otoño'
    elif (mes == 'junio' and dia >= 21) or mes in ['julio', 'agosto'] or (mes == 'septiembre' and dia < 23):
        estacion = 'Invierno'
    elif (mes == 'septiembre' and dia >= 23) or mes in ['octubre', 'noviembre'] or (mes == 'diciembre' and dia < 21):
        estacion = 'Primavera'
    else:
        estacion = 'Verano'
else:
    estacion = 'Hemisferio no válido'

print(f'Usted se encuentra en {estacion}.')