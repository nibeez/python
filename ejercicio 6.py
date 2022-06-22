'''
Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario ingrese el número 0 (detener las preguntas ante este escenario).
'''

num=int(input("Ingrese un numero\n"))
suma=0

while num != 0:
    suma = suma + num
    num=int(input('Ingrese un numero\n'))
print("la suma total es {}".format(suma))