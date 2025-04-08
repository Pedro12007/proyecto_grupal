print("""Sistema de Reserva de Vuelos

Opciones:
    1. Creación de vuelos
    2. Reservar un vuelo
    3. Selección de asiento
    4. Ver reservas
""")

option = input("Ingrese una opción: ")

lista_vuelos = []

if option == '1':
    vuelo = {}

    codigo_vuelo = input("Ingrese un código único de vuelo: ")
    origen = input("Ingrese un origen: ")
    destino = input("Ingrese un destino: ")
    c_asientos = int(input("Ingrese la cantidad de asientos: "))

    vuelo['codigo']=codigo_vuelo
    vuelo['origen']=origen
    vuelo['destino']=destino
    vuelo['cantidad_asientos']=c_asientos
    vuelo['asientos_disponibles']=list(range(1,c_asientos+1))

    lista_vuelos.append(vuelo)
    print(lista_vuelos)