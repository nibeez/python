num=int(input("Ingrese un numero para evaluar\n\n"))

cont=0

for i in range(1,num):
    if num % i == 0:
        cont+=1

if cont!=2:
    print('Numero es primo.')
else:
    print("Numero no es primo.") 