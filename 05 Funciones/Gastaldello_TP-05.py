# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo()

################################################################################

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f'Hola {nombre}, cómo estás?')

nombre_ingresado = input('Ingresa tu nombre: ')
saludo = saludar_usuario(nombre_ingresado)

#############################################################################################

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

ingreso_nombre = input('Ingrese su nombre: ')
ingreso_apellido = input('Ingrese su apellido: ')
ingreso_edad = input('Ingrese su edad: ')
ingreso_residencia = input('Ingrese su residencia: ')

informacion_personal(ingreso_nombre, ingreso_apellido, ingreso_edad, ingreso_residencia)

###############################################################################################

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi

def calcular_area_circulo(radio):
    return(pi * (radio**2))

def calcular_perimetro_circulo(radio):
    return(2 * radio * pi)

ingreso_radio = float(input('Ingrese el radio: '))
area = calcular_area_circulo(ingreso_radio)
perimetro = calcular_perimetro_circulo(ingreso_radio)

print(f'El area del circulo es {area} y el perimetro es de {perimetro}')

################################################################################################

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    return(segundos / 3600)

ingreso_segundos = int(input('Ingrese los segundos: '))
horas = segundos_a_horas(ingreso_segundos)
print(f'Los segundos ingresados corresponden a {horas} horas')

##################################################################################################

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append(numero * i)
    print(f'La tabla de multiplicar del numero ingresado es: {tabla}')

ingreso_numero = int(input('Ingrese un numero: '))
tabla_multiplicar(ingreso_numero)

#####################################################################################################

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por 0"
    return(suma, resta, multiplicacion, division)

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
resultados = operaciones_basicas(num1, num2)
print(f'Los resultados son los siguientes: suma = {resultados[0]}, resta = {resultados[1]}, multiplicacion = {resultados[2]}, division = {resultados[3]}')

####################################################################################################

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f'Su IMC es de {imc:.2f}')

ingreso_peso = float(input('Ingrese su peso en kilos: '))
ingreso_altura = float(input('Ingrese su altura en metros: '))
resultado = calcular_imc(ingreso_peso, ingreso_altura)

#########################################################################################################

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


ingreso_peso = float(input('Ingrese su peso en kilos: '))
ingreso_altura = float(input('Ingrese su altura en metros: '))
imc = calcular_imc(ingreso_peso, ingreso_altura)

print(f'Su IMC es de {imc:.2f}')

###########################################################################################################

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

ingreso_celsius = float(input('Ingrese los grados celsius: '))
fahrenheit = celsius_a_fahrenheit(ingreso_celsius)

print(f'{ingreso_celsius} celsius equivalen a {fahrenheit} fahrenheit')

###########################################################################################################

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input('Ingrese un numero: '))
num2 = float(input('Ingrese otro numero: '))
num3 = float(input('Ingrese un ultimo numero: '))

promedio = calcular_promedio(num1, num2, num3)

print(f'El promedio de los numeros ingresados es {promedio}')