# condicional IF/ELIF/ELSE


        
        
        
        # ejercicio clasicficacion
        
edad = 22
        
if edad < 18:
            
     print("eres menor de edad")
            
elif edad >=18 and edad <= 65:
         print("es adulto")
            
elif edad < 18:
        print("es menor de edad")
            
elif edad > 50:
        print("es adulto mayor")
            
            
            # ejercicio: clasificacion de Edad IF anidado
            
edad  = 15
            
if edad < 18:
    if edad >= 12 and edad <= 17:
            print("eres un adolescente")    
    else:
        print("eres un niño")
else:
    print("eres un adulto")
                
                
    # operaor Ternario
            
numero = 4

if numero % 2 == 0:
    print("el numero es par")
else:
       print("el numero es impar")
                
print("el numero es par" if numero % 2 == 0 else "el numero es impar")
                
            
            
       
            