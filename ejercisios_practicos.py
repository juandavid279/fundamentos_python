# ejercisio 1 

nombre = "juan"
producto = 20000
promedio_asignado=8.5

print("Hola, mi nombre es ", nombre, "y el producto cuesta ", producto, "y el promedio asignado es ", promedio_asignado)


#ejercico 2
# Programa que lee tipos de datos y realiza operaciones

# Lectura de datos
entero1 = int(input("Ingrese el primer entero: "))
entero2 = int(input("Ingrese el segundo entero: "))
numero_float = float(input("Ingrese un número float: "))

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

# Suma de los tres números
suma = entero1 + entero2 + numero_float
print("\nLa suma de los tres números es:", suma)

# Mostrar el entero mayor
if entero1 > entero2:
    print("El entero mayor es:", entero1)
elif entero2 > entero1:
    print("El entero mayor es:", entero2)
else:
    print("Los dos enteros son iguales")

# División del float con el resto de la división de los enteros
resto = entero1 % entero2

if resto != 0:
    resultado = numero_float / resto
    print("Resultado de la división:", resultado)
else:
    print("No se puede dividir entre 0 porque el resto es 0")

# Concatenación de cadenas
concatenacion = cadena1 + " " + cadena2
print("Concatenación de cadenas:", concatenacion)


# ejercisio 3

base = 5
exponente = 3
resultado = base ** exponente
print(F"El resultado de {base} elevado a la {exponente} es {resultado}")



# ejercisio 4

import math

numero = [2, 7 , 10, 15, 20]
for numero in numero :
    raiz = math.sqrt(numero)
    print(F"La raiz cuadrada de {numero} es {raiz}")



# ejercisio 5
nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("\nNombre del estudiante:", nombre)
print("Promedio final:", promedio)

#ejercisio 6

numeroUno = 8
numeroDos = 2

# mostrar valores 

print("valores originales:")
print("numeroUno =", numeroUno)
print("numeroDos =", numeroDos)

auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar

# mostrar resultados

print("/nvalores despues del intercambio:")
print("numeroUno =", numeroUno)
print("numeroDos =", numeroDos)

# ejercisio 7
 
 # crear variable
 
estado = (5 == 2) or (2 > 1)
print("el resultado de la expresion es: ", estado)
 
 
 
 # EJERCICIO 8:

resultado = (20 + 5) * 3 / 5 - 4 + (8 % 3) * 8  - 3 **2

print("El resultado de la expresión es: ", resultado)

 
 #ejercicio 9


# CUADRADO


ladoCuadrado = 8

areaCuadrado = ladoCuadrado * ladoCuadrado
perimetroCuadrado = 4 * ladoCuadrado

print("CUADRADO")
print("Área:", areaCuadrado)
print("Perímetro:", perimetroCuadrado)

# =========================
# TRIÁNGULO
# =========================

baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8

areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
perimetroTriangulo = (
    baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo
)

print("\nTRIÁNGULO")
print("Área:", areaTriangulo)
print("Perímetro:", perimetroTriangulo)

# =========================
# RECTÁNGULO

baseRectangulo = 8
alturaRectangulo = 6

areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print("\nRECTÁNGULO")
print("Área:", areaRectangulo)
print("Perímetro:", perimetroRectangulo)

#ejercicio 10

# Solicitar la edad
edad = int(input("Ingrese la edad de la persona: "))

# Determinar categoría
if 0 <= edad <= 5:
    categoria = "Infante"

elif 6 <= edad <= 10:
    categoria = "Niño"

elif 11 <= edad <= 15:
    categoria = "Pre adolescente"

elif 16 <= edad <= 18:
    categoria = "Adolescente"

elif 19 <= edad <= 25:
    categoria = "Pre adulto"

elif 26 <= edad <= 40:
    categoria = "Adulto"

elif 41 <= edad <= 55:
    categoria = "Pre anciano"

elif edad >= 56:
    categoria = "Anciano"

else:
    categoria = "Edad no válida"

# Mostrar resultado
print("La categoría de la persona es:", categoria)