def obtener_promedio_mensual(temperaturas, ciudad_nombre):
    """ Calcula el promedio mensual de la ciudad ingresada utilizando los datos de temperaturas. """

    # Diccionario de ciudades por índice
    ciudades = ["QUITO", "LOJA", "CUENCA"]

    # Validar si la ciudad ingresada está en la lista
    if ciudad_nombre.upper() not in ciudades:
        return f"La ciudad {ciudad_nombre} no se encuentra en los datos."

    # Obtener el índice de la ciudad
    ciudad_idx = ciudades.index(ciudad_nombre.upper())  

    # Obtener las temperaturas de esa ciudad
    ciudad_temperaturas = temperaturas[ciudad_idx]

    # Calcular el promedio semanal y guardar en una lista
    promedios_semanales = []
    for semana in ciudad_temperaturas:
        suma_temperaturas = sum([dia["temperatura"] for dia in semana])  
        promedio = suma_temperaturas / len(semana)
        promedios_semanales.append(promedio)

    # Calcular el promedio mensual de la ciudad
    promedio_mensual = sum(promedios_semanales) / len(promedios_semanales)


    return {
        "Ciudad": ciudad_nombre.upper(),  # Corregido para mostrar la ciudad en mayúsculas
        "Promedios Semanales": promedios_semanales,
        "Promedio Mensual": promedio_mensual
    }


temperaturas = [
    [  # Quito
        [  # Semana 1
            {"día": "Lunes", "temperatura": 12},
            {"día": "Martes", "temperatura": 14},
            {"día": "Miércoles", "temperatura": 13},
            {"día": "Jueves", "temperatura": 15},
            {"día": "Viernes", "temperatura": 16},
            {"día": "Sábado", "temperatura": 14},
            {"día": "Domingo", "temperatura": 13}
        ],
        [  # Semana 2
            {"día": "Lunes", "temperatura": 11},
            {"día": "Martes", "temperatura": 13},
            {"día": "Miércoles", "temperatura": 12},
            {"día": "Jueves", "temperatura": 14},
            {"día": "Viernes", "temperatura": 15},
            {"día": "Sábado", "temperatura": 13},
            {"día": "Domingo", "temperatura": 12}
        ],
        [  # Semana 3
            {"día": "Lunes", "temperatura": 10},
            {"día": "Martes", "temperatura": 12},
            {"día": "Miércoles", "temperatura": 11},
            {"día": "Jueves", "temperatura": 13},
            {"día": "Viernes", "temperatura": 14},
            {"día": "Sábado", "temperatura": 12},
            {"día": "Domingo", "temperatura": 11}
        ],
        [  # Semana 4
            {"día": "Lunes", "temperatura": 13},
            {"día": "Martes", "temperatura": 15},
            {"día": "Miércoles", "temperatura": 14},
            {"día": "Jueves", "temperatura": 16},
            {"día": "Viernes", "temperatura": 17},
            {"día": "Sábado", "temperatura": 15},
            {"día": "Domingo", "temperatura": 14}
        ]
    ],
    [  # Loja
        [  # Semana 1
            {"día": "Lunes", "temperatura": 16},
            {"día": "Martes", "temperatura": 18},
            {"día": "Miércoles", "temperatura": 17},
            {"día": "Jueves", "temperatura": 19},
            {"día": "Viernes", "temperatura": 20},
            {"día": "Sábado", "temperatura": 18},
            {"día": "Domingo", "temperatura": 17}
        ],
        [  # Semana 2
            {"día": "Lunes", "temperatura": 15},
            {"día": "Martes", "temperatura": 17},
            {"día": "Miércoles", "temperatura": 16},
            {"día": "Jueves", "temperatura": 18},
            {"día": "Viernes", "temperatura": 19},
            {"día": "Sábado", "temperatura": 17},
            {"día": "Domingo", "temperatura": 16}
        ],
        [  # Semana 3
            {"día": "Lunes", "temperatura": 14},
            {"día": "Martes", "temperatura": 16},
            {"día": "Miércoles", "temperatura": 15},
            {"día": "Jueves", "temperatura": 17},
            {"día": "Viernes", "temperatura": 18},
            {"día": "Sábado", "temperatura": 16},
            {"día": "Domingo", "temperatura": 15}
        ],
        [  # Semana 4
            {"día": "Lunes", "temperatura": 17},
            {"día": "Martes", "temperatura": 19},
            {"día": "Miércoles", "temperatura": 18},
            {"día": "Jueves", "temperatura": 20},
            {"día": "Viernes", "temperatura": 21},
            {"día": "Sábado", "temperatura": 19},
            {"día": "Domingo", "temperatura": 18}
        ]
    ],
    [  # Cuenca
        [  # Semana 1
            {"día": "Lunes", "temperatura": 11},
            {"día": "Martes", "temperatura": 13},
            {"día": "Miércoles", "temperatura": 12},
            {"día": "Jueves", "temperatura": 14},
            {"día": "Viernes", "temperatura": 15},
            {"día": "Sábado", "temperatura": 13},
            {"día": "Domingo", "temperatura": 12}
        ],
        [  # Semana 2
            {"día": "Lunes", "temperatura": 10},
            {"día": "Martes", "temperatura": 12},
            {"día": "Miércoles", "temperatura": 11},
            {"día": "Jueves", "temperatura": 13},
            {"día": "Viernes", "temperatura": 14},
            {"día": "Sábado", "temperatura": 12},
            {"día": "Domingo", "temperatura": 11}
        ],
        [  # Semana 3
            {"día": "Lunes", "temperatura": 9},
            {"día": "Martes", "temperatura": 11},
            {"día": "Miércoles", "temperatura": 10},
            {"día": "Jueves", "temperatura": 12},
            {"día": "Viernes", "temperatura": 13},
            {"día": "Sábado", "temperatura": 11},
            {"día": "Domingo", "temperatura": 10}
        ],
        [  # Semana 4
            {"día": "Lunes", "temperatura": 12},
            {"día": "Martes", "temperatura": 14},
            {"día": "Miércoles", "temperatura": 13},
            {"día": "Jueves", "temperatura": 15},
            {"día": "Viernes", "temperatura": 16},
            {"día": "Sábado", "temperatura": 14},
            {"día": "Domingo", "temperatura": 13}
        ]
    ]
]

# Llamada a la función para probar
ciudad_consultada = input("Ingrese la ciudad: ")
resultado = obtener_promedio_mensual(temperaturas, ciudad_consultada)

# Mostrar resultados y usamos el bucle while para tener la opcion de seguir buscando o NO
if isinstance(resultado, dict):
    print(f"Resultados para {resultado['Ciudad']}:")
    print(f"Promedios Semanales: {resultado['Promedios Semanales']}")
    print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")
    consultada1 = input("¿Quisiera seguir buscando? (si/no): ")
    while consultada1.lower() == "si":  
        ciudad_consultada = input("Ingrese la ciudad: ")
        resultado = obtener_promedio_mensual(temperaturas, ciudad_consultada)
        if isinstance(resultado, dict):
            print(f"Resultados para {resultado['Ciudad']}:")
            print(f"Promedios Semanales: {resultado['Promedios Semanales']}")
            print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")
            consultada1 = input("¿Quisiera seguir buscando? (si/no): ")  # Preguntar de nuevo
        else:
            print(resultado)  
            consultada1 = input("¿Quisiera seguir buscando? (si/no): ")  # Preguntar de nuevo
    print("Fin de la búsqueda")
else:
    print(resultado)  
    consultada1 = input("¿Quisiera seguir buscando? (si/no): ")
    while consultada1.lower() == "si":  # ponemos el bucle while para tener la opcion de seguir buscando o NO
        ciudad_consultada = input("Ingrese la ciudad: ")
        resultado = obtener_promedio_mensual(temperaturas, ciudad_consultada)
        if isinstance(resultado, dict):
            print(f"Resultados para {resultado['Ciudad']}:")
            print(f"Promedios Semanales: {resultado['Promedios Semanales']}")
            print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")
            consultada1 = input("¿Quisiera seguir buscando? (si/no): ")  # Preguntar de nuevo
        else:
            print(resultado)  # Mostrar mensaje de error si la ciudad no se encuentra
            consultada1 = input("¿Quisiera seguir buscando? (si/no): ")  # Preguntar de nuevo
    print("Fin de la búsqueda")