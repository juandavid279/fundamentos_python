# operadores arimeticos

import re


a = 5
b = 10

# suma

suma = a + b
print(f"la suma de {a} y {b} es: {suma}")

# resta

resta = a - b
print(f"la resta de {a} y {b} es: {resta}")

# multiplicacion

multiplicacion = a * b
print(f"la multiplicacion de {a} y {b} es: {multiplicacion}")

# division  
division = a / b
print(f"la division de {a} y {b} es: {division}")   

#division entera

division_entera = a // b
print(f"la division entera de {a} y {b} es: {division_entera}")

#division floante o decimal

division_floante = a / b
print(f"la division floante de {a} y {b} es: {division_floante}")   

# modulo   

modulo = a % b
print(f"el modulo de {a} y {b} es: {modulo}")   

# potencia

potencia = a ** b
print(f"la potencia de {a} y {b} es: {potencia}")

# modulo o residuo

modulo = a % b
print(f"el modulo de {a} y {b} es: {modulo}")   

# potencia o exponente

potencia = a ** b
print(f"la potencia de {a} y {b} es: {potencia}")   


#precedncia de operadores 

resultado = a + b * 2
print(f"el resultado de la suma de {a} + {b} * {2} es:{resultado}")

resultado2 = (a + b) * 2
print(f"el resultado de la opreacion de {a} + {b} * {2}: {resultado2}")

resultado3 = a * b // 3 
print(f"el resultado de la operacion de {a} * {b} // {3}: {resultado3}")

resultado4 = (a + b) // 3
print(f"el resultado de la operacion de {a} * {b} // {3}: {resultado4}")


ejercicio = ((a+b) * (a - b) / (a * b)) - ((a ** b) % 3)
# ejercicio = ((3+2) * (3-2) / (3*2) - ((3**2) % 3)
# ejercicio = (5 * 1 / 6) - (9 % 3)
# ejercicio = (5 / 6) - 0
#ejercicio = 0.83333333334

print(f"la suma de la operacion ({a} + {b}) * ({a} - {b}) / ({a} * {b}):es{ejercicio}")

#numero pi
print(math.pi)

#numero aleatorio entre 0 y 10
print(random.random())
numero_aleatorio = random.randint(1, 10) # numero aleatorio entre 1 y 10


