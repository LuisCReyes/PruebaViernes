total_general = 0
dia = 1

while dia <= 3:
    print(f"\nDía {dia}")
    total_dia = 0

    for stand in range(1, 5):  
        print(f"\n  Stand {stand}")
        total_stand = 0

        for producto in range(1, 4): 
            venta = int(input(f"    Ingrese venta del producto {producto}: "))
            total_stand += venta

        print(f"  Total ventas del Stand {stand}: {total_stand}")
        total_dia += total_stand

    print(f"\nTotal ventas del Día {dia}: {total_dia}")
    total_general += total_dia
    dia += 1

print("\n Resumen General de la Feria ")
print("Total de ventas en los 3 días:", total_general)
