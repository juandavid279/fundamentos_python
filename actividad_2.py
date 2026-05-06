# calculadora de notas

print("=" * 40)
print("    CALCULADORA DE NOTAS")
print("=" * 40)

print("\nIngresa tus tres notas parciales (0.0 - 5.0):\n")

nota1 = float(input("  Nota parcial 1: "))
nota2 = float(input("  Nota parcial 2: "))
nota3 = float(input("  Nota parcial 3: "))


promedio = (nota1 + nota2 + nota3) / 3
promedio = round(promedio, 2)   


nota_maxima = 5.0
puntos_faltantes = nota_maxima - promedio
puntos_faltantes = round(puntos_faltantes, 2)


aprueba = promedio >= 3.0


print("\n" + "=" * 40)
print("   RESULTADOS")
print("=" * 40)

print(f"\  Nota 1:          {nota1}")
print(f"  Nota 2:          {nota2}")
print(f"  Nota 3:          {nota3}")
print(f"\  Promedio:        {promedio}")
print(f"  Puntos faltantes para 5.0: {puntos_faltantes}")

print("\n" + "-" * 40)
1
if aprueba:
    print(f"  Estado: APROBADO")
    print(f"  ¡Felicitaciones! Tu promedio de {promedio} es suficiente.")
else:
    print(f"   Estado: REPROBADO")
    print(f"  Tu promedio de {promedio} está por debajo de 3.0.")

print("\n" + "=" * 40)
    
    