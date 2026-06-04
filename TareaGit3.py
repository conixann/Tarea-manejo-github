import os,time

saldo=100000

while True:
    print("Cajero Automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Girar dinero")
    print("4. Salir")
    opc=input("Ingrese opción: ").strip()
    if opc=="1":
        print(f"Saldo disponible: {saldo}")
    elif opc=="2":
        pass
    elif opc=="3":
        pass
    elif opc=="4":
        print("Gracias por haber usado nuestros servicios, adiós,")
        exit
    else:
        pass