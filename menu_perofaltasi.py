#mostrar las opciones de calculo de area, el usuario debe elegir que figura calcular
# 1=cuadrado/rectangulo
# 2=triangulo
# 3=circulo (3,14 * r**2)
# 4=hexagono regular ( 6(((Lado**2)*(3**1/2))/4) )

from pickle import TRUE


def opcion_menu(opc):
    while TRUE:
        if opc==1:
            print("Ha elegido la opcion 1\n")
            side1=float(input("Ingrese lado 1: "))
            side2=float(input("Ingrese lado 2: "))
            area_cuadr=side1*side2
            print(f"El area es {area_cuadr} unidades cuadradas.")
            return area_cuadr
            break
        elif opc==2:
            print('Ha elegido la opcion 2\n')
            side1=int(input("Ingrese lado 1: "))
            side2=int(input("Ingrese lado 2: "))
            area_tri=(side1*side2)/2
            print(f"El area del triangulo es {area_tri} unidades cuadradas.")
            return area_tri
            break
        elif opc==3:
            print("Ha elegido la opcion 3\n")
            side1=int(input("Ingrese el radio del circulo: "))
            area_circ=((side1**2)*pi)
            print(f"El area del circulo es {area_circ} unidades cuadradas.")
            return area_circ
            break
        elif opc==4:
            print("Ha elegido la opcion 4")
            side1=int(input("Ingrese un solo lado del Hexagono: "))
            area_hex=6*((side1**2)*(3**(1/2))/4)
            print(f'El area del hexagono es {area_hex} unidades cuadradas')
            return area_hex
            
        else:
            print("Valor invalido")
            opc=int(input('Vuelva a ingresar un valor.'))

print('''
Que area desea calcular?
1=cuadrado/rectangulo
2=triangulo
3=circulo
4=hexagono regular''')
n=int(input(''))
side1=0
side2=0
pi=3.14

opcion_1=opcion_menu(n)