suma_notas=0
promedio=0
while True:
    try:
        cant_notas=int(input("Ingrese cantidad de notas a promediar:"))
        if cant_notas>0:
            break
    except ValueError:
        print("Error, ingrese un número entero positivo!")

for x in range(cant_notas):
    while True:
        try:
            nota=float(input(f"Ingrese la nota {x+1}:"))
            if nota > 0:
                break
            else: 
                print("La nota ingresada debe ser un número positivo")
        except ValueError:
            print("Error ingrese un número positivo (entero o decimal)")

        suma_notas += nota

promedio= suma_notas/cant_notas

print(promedio)