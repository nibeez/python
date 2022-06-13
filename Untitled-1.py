from operator import invert


def eliminarEspacios(cad):
    cad_nueva=""
    for letra in cad:
        if letra!=" ":  #if letra not in " ":
            cad_nueva=cad_nueva+letra
    return cad_nueva

def invertirCadena(cad):
    cad_nueva=""
    for letra in cad:
        cad_nueva=letra+cad_nueva
    return cad_nueva

def palindromoCadena(cad):
    test = eliminarEspacios(cad)
    
    test = invertirCadena(test)
    print(cad,test)
    if eliminarEspacios(cad) == test:
        print("si es palindroma ")
    else:
        print("No es palindromo")
    
    

cadena=input("ingresa cadena \n")
#necesitamos eliminar los espacios
#sinBlancos=eliminarEspacios(cadena)
#print(sinBlancos)

#cadInvertida=invertirCadena(cadena)
#print(cadInvertida)
palindromoCadena(cadena)
#diseñar una def q permita evaluar si la cadena ingresada
#es un palindromo
