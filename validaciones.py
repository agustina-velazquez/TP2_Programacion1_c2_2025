

def validar_rango_posicion(posicion, posicion_inicial, posicion_final):
    while posicion < posicion_inicial or posicion > posicion_final:
        posicion = int(input("La posicion no esta dentro del rango. Ingrese una posicion valida: "))

    return posicion
    
def validar_repeticion_de_posicion(usadas, posicion):
    while posicion in usadas:
        posicion = int(input("Esa posicion ya fue usada. Elija otra: "))
    
    return posicion

