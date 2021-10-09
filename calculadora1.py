def suma():
    print('---------------------------')
    print('Digite su primer numero:')
    n1=float(input())
    print('Digite su segundo numero:')
    n2=float(input())
    op_suma=n1+n2
    print('---------------------------')
    print('Su resultado --> '+str(op_suma))
    menu()

def resta():
    print('---------------------------')
    print('Digite su primer numero:')
    n1=float(input())
    print('Digite su segundo numero:')
    n2=float(input())
    op_resta=n1-n2
    print('---------------------------')
    print('Su resultado --> '+str(op_resta))
    menu()

def multiplicacion():
    print('---------------------------')
    print('Digite su primer numero:')
    n1=float(input())
    print('Digite su segundo numero:')
    n2=float(input())
    op_multiplicacion=n1*n2
    print('---------------------------')
    print('Su resultado --> '+str(op_multiplicacion))
    menu()

def division():
    print('---------------------------')
    print('Digite su primer numero:')
    n1=float(input())
    print('Digite su segundo numero:')
    n2=float(input())
    if n2==0:
        print('---------------------------')
        print('Porfavor, digite un numero valido.')
        division()
    op_division=n1/n2
    print('---------------------------')
    print('Su resultado --> '+str(op_division))
    menu()

def menu():
    menu = """
    CALCULADORA BASICA
    ---------------------------------------------------
    DIGITE SU OPERACION A REALIZAR:
    1) Suma.
    2) Resta.
    3) Multiplicacion.
    4) Division.
    5) Salir.
    ---------------------------------------------------
    """
    print(menu)

    op=int(input("Opcion: "))

    if op == 1:
        suma()
    elif op == 2:
        resta()
    elif op ==3:
        multiplicacion()
    elif op ==4:
        division()
    elif op==5:
        quit()
    else:
        print('----------------------')
        print("Opcion erronea.")
        print('----------------------')
        menu()
        
menu ()