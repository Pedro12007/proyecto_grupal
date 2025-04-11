lista_vuelos = []
codigos_unicos = []
reservas = []

while True:
    print("""\n------------------------------------------------------------
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

        while True:
            codigo_vuelo = input("Ingrese un código único de vuelo: ")
            if not(codigo_vuelo in codigos_unicos):
                codigos_unicos.append(codigo_vuelo)
                break
            else: 
                print("El código ya ha sido utilizado, cree uno nuevo.\n")

        origen = input("Ingrese un origen: ")
        destino = input("Ingrese un destino: ")

        while True:
            c_asientos = input("Ingrese la cantidad de asientos: ")
            if c_asientos.isdigit() and int(c_asientos)>=1:
                c_asientos = int(c_asientos)
                break
            else: 
                print('Cantidad o formato invalido, intente de nuevo.\n')

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
            print("VUELOS: ")    
            for i, vuelos in zip(range(len(lista_vuelos)+1), lista_vuelos):
                print(f'{i}. Código de vuelo: {vuelos['codigo']}. Viaje de: {vuelos['origen']} a {vuelos['destino']}. Asientos disponibles: {list(vuelos['asientos_disponibles'].values()).count(1)}')

            while True:
                e_vuelo = input("Ingrese el vuelo que desea tomar por númeración: ")
                if e_vuelo.isdigit() and int(e_vuelo) >= 0 and int(e_vuelo) <= len(lista_vuelos)-1:
                    e_vuelo = int(e_vuelo)
                    break
                else:
                    print("Vuelo inexistente. Intente de nuevo.\n")

            print('\nASIENTOS: 1=Disponible 0=Ocupado')
            print(lista_vuelos[e_vuelo]['asientos_disponibles'])
            
            while True:
                asiento = input("Ingrese el asiento que desea reservar: ")
                if asiento.isdigit() and int(asiento) >= 1 and int(asiento) <= len(lista_vuelos[e_vuelo]['asientos_disponibles']): #Verifica que el asiento exista
                    asiento = int(asiento)
                    if lista_vuelos[e_vuelo]['asientos_disponibles'][asiento] == 1: #Verifica si está disponible
                        lista_vuelos[e_vuelo]['asientos_disponibles'][asiento] = 0

                        print(f'Asiento "{asiento}" reservado exitosamente.')
                        reserva = [e_vuelo, asiento]
                        reservas.append(reserva)
                        break

                    elif lista_vuelos[e_vuelo]['asientos_disponibles'][asiento] == 0: #Verifica si está ocupado
                        print('Asiento ocupado.\n')

                else:
                    print("Asiento inexistente. Intente de nuevo\n")

    if option == '3': #Ver reservas 
        if len(reservas) == 0:
            print("No hay reservas.")
        elif len(reservas) >= 1:
            print("RESERVAS: ")
            for i, reserva in zip(range(len(reservas)+1), reservas):
                print(f'{i}. Código de vuelo: {lista_vuelos[reserva[0]]['codigo']}. Asiento reservado: {reserva[1]}' )


            eleccion = input("\n¿Desea cambiar asiento en alguna reserva? (1:si / otro caracter:no): ")
            
            if eleccion == '1':
                while True:
                    e_reserva = input('Seleccione una reserva por númeración: ')
                    if e_reserva.isdigit() and int(e_reserva)>=0 and int(e_reserva) <= len(reservas)-1:
                        e_reserva = int(e_reserva)

                        print('\nASIENTOS: 1=Disponible 0=Ocupado')
                        print(lista_vuelos[reservas[e_reserva][0]]['asientos_disponibles'])

                        while True:
                            asiento = input("Ingrese el asiento que desea reservar: ")
                            if asiento.isdigit() and int(asiento) >= 1 and int(asiento) <= len(lista_vuelos[reservas[e_reserva][0]]['asientos_disponibles']): #Verifica que el asiento exista
                                asiento = int(asiento)
                                if lista_vuelos[reservas[e_reserva][0]]['asientos_disponibles'][asiento] == 1: #Verifica si está disponible
                                    lista_vuelos[reservas[e_reserva][0]]['asientos_disponibles'][asiento] = 0                        
                                    lista_vuelos[reservas[e_reserva][0]]['asientos_disponibles'][reservas[e_reserva][1]] = 1

                                    reservas[e_reserva][1] = asiento

                                    print(f'Asiento "{asiento}" reservado exitosamente.')
                                    break

                                elif lista_vuelos[reservas[e_reserva][0]]['asientos_disponibles'][asiento] == 0: #Verifica si está ocupado
                                    print('Asiento ocupado.\n')
                        
                            else:
                                print("Asiento inexistente. Intente de nuevo.\n")

                        break

                    else:
                        print("Reserva inexistente. Intente de nuevo.\n")

                        

    if option == '4':
        break

    if not(option in '1234'):
        print('Opcion invalida.')