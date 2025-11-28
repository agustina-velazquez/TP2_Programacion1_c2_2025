posiciones = [0,1,2,3,4,5]

def validar_posicion(posicion, posicion_inicial, posicion_final):
    while posicion < posicion_inicial or posicion > posicion_final:
        posicion = int(input("La posicion no esta dentro del rango. Ingrese una posicion valida: "))

    return posicion
    

    

