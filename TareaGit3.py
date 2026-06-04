import os,time

saldo=100000
os.system('cls')
while True:
    print("Cajero Automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Girar dinero")
    print("4. Salir") 
    opc=input("Ingrese opción: ").strip()
    
    if opc=="1":
        os.system('cls')
        print(f"Saldo disponible: {saldo}")
        time.sleep(3)
    elif opc=="2":
        os.system('cls')
        while True:
            try:
                deposito=int(input("¿Cuanto dinero desea ingresar?:"))
                if deposito > 0:
                    saldo += deposito
                    print(f"Saldo actual: {saldo}")
                    time.sleep(3)
                    break
            except ValueError:
                print("ERROR! Ingrese un número entero positivo!")
    elif opc=="3":
        os.system('cls')
        while True:
            try:
                giro=int(input("¿Cuanto dinero desea retirar?:"))
                if giro > saldo:
                    print("Error, excede el máximo de saldo disponible.")
                elif giro > 0:
                    saldo -= giro
                    print(f"Saldo actual: {saldo}")
                    time.sleep(3)
                    break
    
            except ValueError:
                print("ERROR! ingresa un número entero positivo")
                time.sleep(3)
    elif opc=="4":
        os.system('cls')
        print("Gracias por haber usado nuestros servicios, adiós.")
        time.sleep(3)
        
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        time.sleep(2)