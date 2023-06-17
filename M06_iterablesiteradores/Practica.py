
def contar_silabas(palabra):
    diccionario_silabas = pyphen.Pyphen(lang='es')  # Cargamos el diccionario de sílabas en español
    
    silabas = diccionario_silabas.inserted(palabra)  # Separamos la palabra en sílabas
    
    lista_silabas = silabas.split('-')  # Convertimos las sílabas en una lista
    
    cantidad_silabas = len(lista_silabas)  # Contamos la cantidad de sílabas
    
    return lista_silabas, cantidad_silabas

# Pedimos al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Llamamos a la función para contar las sílabas
resultado_silabas, cantidad_silabas = contar_silabas(palabra)

# Imprimimos las sílabas y la cantidad
print("Sílabas:", resultado_silabas)
print("Cantidad de sílabas:", cantidad_silabas)
