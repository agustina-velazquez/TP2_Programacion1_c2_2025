import random
import validaciones


def tirar_dados(numero_de_dados, cara_inicial, cara_final):

    lista_auxiliar = []
   
    for i in range(numero_de_dados):
        
        lista_auxiliar.append(random.randint(cara_inicial, cara_final))
    
    print(f"tirada de dados: {lista_auxiliar}")

    
    return lista_auxiliar
        


def elegir_dados(lista_auxiliar):

    dados_elegidos = []
    
    for i in range(len(lista_auxiliar)):  

        posicion = input("Ingrese posicion que desea conservar, o ENTER para no conservar: ")

        if not posicion.isdigit():

            return dados_elegidos
        
        posicion = validaciones.validar_posicion(int(posicion), 0, len(lista_auxiliar)-1)
    

        dados_elegidos.append(lista_auxiliar[posicion])
        print(f"los elegidos son: {dados_elegidos}")

    return dados_elegidos
        

def armar_lista_final(tiros,numero_de_dados,cara_inicial,cara_final):
    lista_final = []
    lista_auxiliar = []
    dados_elegidos = []

    while tiros > 0:

        lista_auxiliar = tirar_dados(numero_de_dados, cara_inicial, cara_final)
        dados_elegidos = elegir_dados(lista_auxiliar)
        numero_de_dados = numero_de_dados - len(dados_elegidos)
        lista_final.extend(dados_elegidos)

        tiros = tiros - 1

    while len(lista_final) < 5:
        print("Debe elegir mas dados.")
    

        if dados_elegidos == []:
            dados_elegidos = elegir_dados(lista_auxiliar)
            lista_final.extend(dados_elegidos)
        
        a = set(lista_auxiliar)
        b = set(dados_elegidos)
        lista_auxiliar = list(a.difference(b))
        print(f"los restantes son: {lista_auxiliar}")

        dados_elegidos = elegir_dados(lista_auxiliar)
       
        lista_final.extend(dados_elegidos)
        
            
    return lista_final
   
print(armar_lista_final(3, 5, 1, 6))







