nombre = ""
while len(nombre) < 6:
    nombre = input("Indique su nombre y apellido: ") #Esto pide el nombre y apellido del usuario
    if len(nombre) > 6:
        break
    print("Tu nombre y apellido deberia ser mas largo") # El Nombre con apellido debe tener mas de 5 caracteres
HorasT = 0
while HorasT <= 0:
    HorasT = int(input("Indique las horas trabajadas: ")) #Esto pide las horas trabajadas
    if HorasT <= 0:
        print("Coloque un numero mayor que 0")
SueldoB = HorasT * 9500 #Se multiplican las horas trabajadas con el precio por hora 
SueldoIn = SueldoB #Aca se guarda el sueldo Bruto del trabajador
while True:
    print("1. Isapre")
    print("2. Fonasa")
    IsOrFon = int(input("Seleccione el numero correspondiente: ")) #Se le pregunta al usuario si tiene isapre o fonasa
    if IsOrFon == 1 or IsOrFon == 2:
        break
if IsOrFon == 1:
    while True: 
        print("1. Mas vida");print("2. Consalud");print("3. Colmena");print("4. Banmedica");print("5. Cruz Blanca");print("6. Vida Tres") #Se abre un menu de diferentes isapres
        NumIs = int(input("Seleccione Su Isapre:")) #Seleccion de isapre
        if NumIs > 0 and NumIs <= 6:
            break 
    if NumIs == 1:                       #Inicio descuentos isaspres
        DesIsapre = 32500 * 2 #conversion UF para descuento
        SueldoB= SueldoB - DesIsapre #Se aplica el descuento
        Isapre = "Mas vida"
    elif NumIs == 2:
        DesIsapre = 32500 * 2
        SueldoB= SueldoB - DesIsapre
        Isapre = "Consalud"
    elif NumIs == 3:
        DesIsapre = 32500 * 2.11
        SueldoB= SueldoB - DesIsapre
        Isapre = "Colmena"
    elif NumIs == 4:
        DesIsapre = 32500 * 2.34
        SueldoB= SueldoB - DesIsapre
        Isapre = "Banmedica"
    elif NumIs == 5:
        DesIsapre = 32500 * 2.76
        SueldoB= SueldoB - DesIsapre
        Isapre = "Cruz Blanca"
    elif NumIs == 6:
        DesIsapre = 32500 * 2.78
        SueldoB= SueldoB - DesIsapre
        Isapre = "Vida Tres"
elif IsOrFon == 2: #En caso de que escoga fonasa se aplica el siguiente cambio
    fonasa = SueldoIn * (7 / 100) #Se obtiene el 7% del descuento
    SueldoB -= fonasa # se aplica el descuento
desAFP = SueldoIn * 0.12 #Se busca el 12% del descuento afp
SueldoB -= desAFP #Se aplica el descuento de afp
DesAFC = SueldoIn * (3 / 100) #Se Busca el 3% Descuento AFC
SueldoB -= DesAFC #Se aplica el descuento AFC
print("El Sueldo del Sr/a",nombre," Es:")      #Se abre el menu de descuentos
print("Sueldo Bruto: ",SueldoIn)
print("Sueldo Liquido: ", SueldoB)
print("Descuento AFP: ", desAFP)
print("Descuento AFC: ", DesAFC)
if IsOrFon == 1:   #Se muestra el descuento segun que escogio el usuario isapre o fonasa
    print("El descuento de isapre es: ",DesIsapre)
else:
    import math
    fonasa = math.trunc(fonasa) #Se aplica un truncado a fonasa (para que el resultado no quede como 0.0000001)
    print("El descuento de fonasa es:",fonasa )