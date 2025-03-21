def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando un porcentaje al monto total.

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def insertar_datos_de_la_factura():
    # Funcion que permite al usuario ingresar los datos de los productos de la factura.
    # con una lista vacia que almacenar los productos de la factura
    factura = []
    # usamos una variable para preguntar al usuario si decea poner mads datos
    continuar = "si"
    # Usamos el bucle while que permite ingresar múltiples productos mientras el usuario lo desee
    while continuar.lower() == "si":
        # Almacena la cantidad del producto.
        cantidad = int(input("Ingrese la cantidad: "))
        # Almacena la descripción del producto.
        descripcion = input("Ingrese qué ha comprado el cliente: ")
        # Almacena el precio unitario del producto.
        precio_unitario = float(input("Ingrese el precio unitario: "))
        # Almacena el precio total del producto.
        precio_total = cantidad * precio_unitario

        # Agrega los datos del producto a la lista como un diccionario.

        factura.append({
            # Almacena la cantidad del producto.
            "cantidad": cantidad,
            # Almacena la descripción del producto.
            "descripcion": descripcion,
            # Almacena el precio unitario del producto.
            "precio_unitario": precio_unitario,
            # Almacena el precio total del producto.
            "precio_total": precio_total
        })
        # Pregunta al usuario si desea ingresar más productos.
        continuar = input("¿Insertará más datos a la factura? si/no: ")

    # Devuelve la lista completa de productos ingresados.
    return factura


def main():
    # Función principal que ejecuta el programa.
    print("Ingreso de datos para la factura:")
    factura = insertar_datos_de_la_factura()

    monto_total = sum(item["precio_total"] for item in factura)
    print("\nFactura Generada:")
    for item in factura:
        print(
            f"{item['cantidad']} x {item['descripcion']} - ${item['precio_unitario']} c/u - Total: ${item['precio_total']}")
    print(f"Monto total sin descuento: ${monto_total}\n")

    # Primera llamada a calcular_descuento con el porcentaje predeterminado 10%
    descuento1 = calcular_descuento(monto_total)
    # Muestra el monto del descuento aplicado y el monto final después del descuento
    monto_final1 = monto_total - descuento1
    print(f"Descuento aplicado (10% predeterminado): ${descuento1}")
    print(f"Monto final después del descuento: ${monto_final1}\n")

    # Segunda llamada a calcular_descuento con un porcentaje personalizado
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento que desea aplicar: "))
    # Calcula el monto del descuento aplicando el porcentaje ingresado al monto total de la compra.
    descuento2 = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final2 = monto_total - descuento2
    # Imprime el monto del descuento aplicado y el porcentaje utilizado.
    print(f"Descuento aplicado ({porcentaje_descuento}%): ${descuento2}")
    print(f"Monto final después del descuento: ${monto_final2}")

    # Verifica si el script se está ejecutando como el programa principal.


if __name__ == "__main__":
    main()