# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    # Escribimos la primera línea de notas en el archivo
    file.write("Nota 1: ir a la tienda y realizar la compra de la lista.\n")  
    # Escribimos la segunda línea de notas en el archivo
    file.write("Nota 2: pasate por la pasteleria y compra el pastel.\n") 
     # Escribimos la tercera línea de notas en el archivo
    file.write("Nota 3: ir por farmacia para traer la receta de tu hermano.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    for line in file:
         # Imprimimos cada línea en la consola, eliminando el salto de línea al final
        print(line.strip())  # Imprimir cada línea sin saltos de línea adicionales