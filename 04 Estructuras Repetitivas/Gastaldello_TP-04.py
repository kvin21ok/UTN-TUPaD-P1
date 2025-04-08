# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

#############################################################################################

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num = int(input('Ingrese un numero: '))

if num == 0:
    cant_digitos = 1
else:
    cant_digitos = 0
    while num > 0:
        num //= 10
        cant_digitos += 1

print(f'La cantidad de digitos que tiene el numero ingresado es {cant_digitos}')

################################################################################################

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range (num1 +1, num2):
    suma += i

print(f'La suma de los numeros comprendidos entre el primero y el segundo ingresado sin incluirlos es de {suma}')

##################################################################################################

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
ingreso = int(input('Ingrese un numero (0 para terminar el bucle): '))
suma = 0

while ingreso != 0:
    suma += ingreso
    ingreso = int(input('Ingrese un numero (0 para terminar el bucle): '))

print(f'La suma de los numeros ingresados es {suma}')

####################################################################################################

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

num_random = random.randint(0, 9)
ingreso = int(input('Adivine el numero random entre 0 y 9: '))
suma = 1

while ingreso != num_random:
    ingreso = int(input('Adivine el numero random entre 0 y 9: '))
    suma +=1

print(f'El numero random era {num_random}. Fueron necesarios {suma} intentos para adivinar el numero random')

#####################################################################################################

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, 0, -2):
    print(i)

#####################################################################################################

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
ingreso = int(input('Ingrese un numero: '))

suma = ingreso # se puede hacer asi para que no sea necesario agregar un paso extra en el extremo final del range ya que de esta manera ya me lo tiene en cuenta a ese valor
for i in range(0, ingreso):
    suma += i

print(f'La suma de todos los numeros comprendidos entre 0 y {ingreso} es {suma}')

################################################################################################################

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
contador = 0
pares = 0
impares = 0
negativos = 0
positivos = 0

while contador < 5:
    ingreso = int(input('Ingrese un numero: '))
    contador += 1
    if (ingreso % 2 == 0):
        pares += 1
    else:
        impares += 1
    if ingreso > 0:
        positivos += 1
    else:
        negativos += 1

print(f'Pares: {pares} // impares: {impares} // positivos {positivos} // negativos: {negativos}')

###############################################################################################################

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
contador = 0
numeros = []

while contador < 5: # se cambia el valor de la condicion para poder procesar mas numeros si es necesario
    ingreso = int(input('Ingrese un numero: '))
    contador += 1
    numeros.append(ingreso)
suma = sum(numeros)
media = suma / contador

print(f'La media de los numeros ingresados es {media}')

##############################################################################################################3

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
ingreso = int(input('Ingrese un numero para poder invertir sus digitos: '))
invertido = 0

while ingreso > 0:
    digito = ingreso % 10 # aca sacamos el ultimo digito del ingreso mediante el resto de la division
    invertido = invertido * 10 + digito # esta parte va armando el numero invertido
    ingreso //= 10 # ingreso pasa a ser el numero original menos el ultimo numero que ya lo sacamos en la variable 'digito'

print(f'El numero invertido es {invertido}')