total_discount=0
while True:
    product=input("Ingrese nombre de el producto: ").strip().title()
    if len(product) >3:
        break
    else:
        print("Error, el producto contiene muy pocos caracteres. ")
while True:
    try:        
        price=int(input("Ingrese el precio de el producto: "))
        if price > 0:
            break
        else:
            print("El precio debe ser un número entero positivo mayor a 0")
    except ValueError:
        print("Error, Ingrese un número entero")
while True:
    try:
        discount=int(input("Ingrese el descuento al producto:"))
        if discount >= 50:
                warning=input("El descuento es igual o mayor a el 50% ¿Estas seguro que lo deseas aplicar? (S/N): ").upper().strip()
                if warning == "S":
                    break
                else: 
                    continue
        elif discount >0:
            break
        else: 
            print("Error, el descuento debe ser mayor que 0")
    except ValueError:
        print("Error, ingresaste caracteres inválidos, ingresa solo números positivos")

total_discount= int(price * (1 - discount/100))


print(f"Producto: {product}")
print(f"Precio original: {price}")
print(f"Descuento: {discount}")
print(f"Precio final: {total_discount} ")
