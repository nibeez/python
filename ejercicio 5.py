'''
Escriba un algoritmo que calcule e imprima la suma de los n primeros números enteros positivos. El valor de n debe leerse del teclado y ser ingresado por el usuario
'''

num=int(input('Ingrese un numero cualquiera: \n'))
suma = 0
for i in range(num+1):
    suma = suma + i
print("la suma es {}".format(suma))