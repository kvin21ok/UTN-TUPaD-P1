# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print('Hola Mundo!')

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input ('Por favor ingrese su nombre: ')
print(f'Hola {nombre}!')

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input ('Por favor ingrese su nombre: ')
apellido = input ('Por favor ingrese su apellido: ')
edad = input ('Por favor ingrese su edad: ')
residencia = input ('Por favor ingrese su ciudad de residencia: ')
print(f'Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = float(input('ingrese el radio del circulo para calcular su area: '))
area = (radio * radio) * 3.14
print(f'el area del circulo es de {area}')

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = float(input('Ingrese la cantidad de segundos: '))
horas = segundos / 60
print(f'Los segundos ingresados corresponden a {horas} hora/s')

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input('Ingrese un numero para devolverle su tabla de multiplar: '))
tabla = []
for i in range (1, 11):
    tabla.append(numero * i)
print(f'La tabla del {numero} es {tabla}')

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input('Ingrese un numeros DISTINTO de 0: '))
num2 = int(input('Ingrese otro numeros DISTINTO1 de 0: '))
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2
print(f'La suma de esos numeros da {suma}, su resta es {resta}, la multiplicacion es igual a {multiplicacion} y su division es {division}')

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.
altura = float(input('Ingrese su altura EN METROS: '))
peso = float(input('Ingrese su peso EN KILOS: '))
IMC = peso / (altura **2)
print(f'Su IMC es de {IMC}')

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.
celsius = float(input('Ingrese los grados celsius a convertir en fahrenheit: '))
fahrenheit = ((9/5) * celsius) + 32
print(f'La temperatura en fahrenheit es de {fahrenheit}')

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))
num3 = int(input('Ingrese un tercer numero: '))
promedio = (num1 + num2 + num3) / 3
print(f'El promedio de los tres numeros ingresados es {promedio}')