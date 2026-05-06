

a = float(input("ingrese un numero: "))
b = float(input("ingrese otro numero: "))
tipo_de_operacion = input("ingrese el tipo de operacion que desea realizar: 1.suma 2.resta 3.multiplicacion 4.division 5.modulo 6.potencia: ")


suma = a + b
resta = a - b
multiplicacion = a *  b
division = a / b
modulo = a % b
potencia = a ** b
 
if tipo_de_operacion == "1":
    print("la suma es: ",suma)
elif tipo_de_operacion == "2":
    print("la resta es: ",resta)
elif tipo_de_operacion == "3":
    print("la multiplicacion es: ",multiplicacion)
elif tipo_de_operacion == "4":
    print("la division es: ",division)
elif tipo_de_operacion == "5":
    print("el modulo es: ",modulo)
elif tipo_de_operacion == "6":
    print("la potencia es: ",potencia)

