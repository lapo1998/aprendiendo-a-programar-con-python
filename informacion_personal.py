# 1. Creamos un Diccionario:

def cambiar_ciudad(informacion_personal):
    ciudad = input("Ingresar el nombre de la nueva ciudad: ")
    informacion_personal["ciudad"] = ciudad
    return informacion_personal # Devuelve el diccionario modificado.

informacion_personal = {  # Creamos un diccionario llamado informacion_personal
    "nombre": "Elvio Manuel",
    "edad": 26,
    "ciudad": "loja",
    "profesion": "estudiante Ingeniera"
}

# 2. Acceder y Modificar Valores:

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Loja"

# Agregar una nueva clave - valor al diccionario que represente la "profesion" de la persona.
informacion_personal["profesion"] = "estudiante de tecnologias de la informacion"

# 3. Verificar Existencia de Claves:
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999988122"

# Imprimir el diccionario final (esto se mostrará al inicio)
print("Datos iniciales del diccionario:") # Imprime la cadena "Datos iniciales del diccionario:".
print(informacion_personal) # Imprime el contenido del diccionario informacion_personal.
print("\n")

def menu_principal():
    print("-----------Bienvenido al SGA------------")
    print("----Menu Principal----")
    print("1.- Crear Nueva Persona") # Imprime la cadena: Crear Estudiantenueva persona".
    print("2.- Agregar Información Adicional") # Imprime la cadena: Agregar Información Adicional".
    print("3.- Actualizar Información Existente")# Imprime la cadena: Actualizar Información Existente".
    print("4.- Mostrar Información Específica") # Imprime la cadena: Mostrar Infor  mación Específica".
    print("5.- Imprimir Datos de Persona") # Imprime la cadena: Imprimir Datos de Persona".
    print("6.- Salir")                   # Imprime la cadena: Salir".
    return int(input("Ingrese una opcion: ")) # Solicita al usuario que ingrese una opción, la convierte a entero y la devuelve.


def imprimir_informacion_personal(info): # Define una función llamada imprimir_informacion_personal que toma un diccionario como argumento.
    print("Datos de la Persona") # Imprime datos de la persona
    for clave, valor in info.items(): 
        print(f"- {clave}: {valor}") # Imprime la clave y el valor de cada elemento del diccionario.

def crear_nueva_persona():
    nueva_persona = {}
    nueva_persona["nombre"] = input("Ingrese el nombre: ") # Solicita al usuario que ingrese el nombre 
    nueva_persona["edad"] = int(input("Ingrese la edad: ")) # Solicita al usuario que ingrese la edad
    nueva_persona["ciudad"] = input("Ingrese la ciudad: ") # Solicita al usuario que ingrese la ciudad
    nueva_persona["profesion"] = input("Ingrese la profesión: ") # Solicita al usuario que ingrese la profesión
    return nueva_persona

def agregar_informacion_adicional(info):
    clave = input("Ingrese la clave del nuevo dato: ") # Solicita al usuario que ingrese la clave del nuevo dato.
    valor = input("Ingrese el valor del nuevo dato: ") # Solicita al usuario que ingrese la clave del nuevo dato.

    info[clave] = valor
    print("Información adicional agregada correctamente.")

def actualizar_informacion_existente(info):
    clave = input("Ingrese la clave del dato que desea actualizar: ") # Solicita al usuario que ingrese la clave del dato a actualizar
    if clave in info:                                                 # Verifica si la clave existe en el diccionario
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}': ") # Solicita al usuario que ingrese el nuevo valor para la clave especificada
        info[clave] = nuevo_valor                                       # Actualiza el valor de la clave en el diccionario
        print("Información actualizada correctamente.")                 # Imprime un mensaje indicando que la información se actualizó correctamente
    else:
        print(f"La clave '{clave}' no existe en la información.")

def mostrar_informacion_especifica(info):
    clave = input("Ingrese la clave de la información que desea ver: ") # Solicita al usuario que ingrese la clave de la información que desea ver.
    if clave in info:                                                 #Verifica si la clave existe en el diccionario 
        print(f"{clave}: {info[clave]}")                                # Imprime la clave y su valor correspondiente.
    else:
        print(f"La clave '{clave}' no existe en la información.")    # Imprime un mensaje indicando que la clave no existe.

if __name__ == "__main__":                                           # Verifica si el script se está ejecutando directamente.
    while True:                                                    # Inicia un bucle infinito.
        opcion = menu_principal()
        if opcion == 1:                                          # Verifica si la opción es 1
            informacion_personal = crear_nueva_persona()
            print("Nueva persona creada.")                   # Imprime un mensaje indicando que se creó nueva persona.
            imprimir_informacion_personal(informacion_personal)
        elif opcion == 2:
            agregar_informacion_adicional(informacion_personal)
        elif opcion == 3:
            actualizar_informacion_existente(informacion_personal)
        elif opcion == 4:
            mostrar_informacion_especifica(informacion_personal)
        elif opcion == 5:
            imprimir_informacion_personal(informacion_personal)
        elif opcion == 6:
            print("Gracias por su colaboración") # Imprime un mensaje de agradecimiento.
            break                               # Sale del bucle while, terminando el programa.
        else:                                 #Si la opción ingresada no es válida.
            print("No existe esa opción")        # Imprime un mensaje indicando que la opción no es válida.