# Creamos una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades: Quito-Loja-cuenca)
# los 7 dias de la semana
# por 4 semanas
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

def calcular_promedio_temperaturas(temperaturas):
    ciudades = ["Quito", "Loja", "Cuenca"]
    for ciudad_idx, ciudad in enumerate(temperaturas):
        for semana_idx, semana in enumerate(ciudad):
            total_temperatura = 0
            for dia in semana:
                total_temperatura += dia["temperatura"]
            promedio = total_temperatura / len(semana)
            print(f"{ciudades[ciudad_idx]}, Semana {semana_idx + 1}: Promedio = {promedio:.2f} grados")