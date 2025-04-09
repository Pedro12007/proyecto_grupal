lista_vuelos = []

while True:
    print("""\n-----------------------------------------
Sistema de Reserva de Vuelos

    Opciones:
        1. Creación de vuelos
        2. Reservar un vuelo
        3. Ver reservas
        4. Salir
    """)

    option = input("Ingrese una opción: ")
    print()

    if option == '1': #Creación de vuelos
        vuelo = {}

        codigo_vuelo = input("Ingrese un código único de vuelo: ")
        origen = input("Ingrese un origen: ")
        destino = input("Ingrese un destino: ")
        c_asientos = int(input("Ingrese la cantidad de asientos: "))

        vuelo['codigo']=codigo_vuelo
        vuelo['origen']=origen
        vuelo['destino']=destino
        vuelo['cantidad_asientos']=c_asientos
        vuelo['asientos_disponibles']={}
        
        for i in range(1, c_asientos+1):
            vuelo['asientos_disponibles'][i]=1

        lista_vuelos.append(vuelo)

    if option == '2': #Reservación de vuelos
        if len(lista_vuelos)==0:
            print("No hay vuelos disponibles")
        elif len(lista_vuelos)>=1:    
            for vuelos in lista_vuelos:
                print(f'Código de vuelo: {vuelos['codigo']}. Viaje de: {vuelos['origen']} a {vuelos['destino']}. Asientos disponibles: {list(vuelos['asientos_disponibles'].values()).count(1)}')



    if option == '4':
        break