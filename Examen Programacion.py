def stock_marca():  # Función que inicializa la opción 1 del menú
    contador = 0  # Contador que permite sumar la cantidad de stock
    marca_busqueda = input("Ingrese marca a consultar: ") 
    marca_busqueda = marca_busqueda.upper()  #convierte la respuesta del usuario a mayusculas

    ls_concidencia = []  #crea una lista para añadir todas las coincidencias de la marca

    for marca in productos:  #Busca la variable "marca" en el diccionario de productos
        if marca["marca"].upper() == marca_busqueda:  #Si hay coincidencias, realiza el proceso de abajo. Cambia la marca ingresada a mayusculas
            sku = marca["SKU"]  #renombra la variable "sku" segun el SKU del producto que coincidio
            ls_concidencia.append(sku)  #Añade el SKU que coincide a la lista

    if ls_concidencia: 
        for sku in stock:  #busca la variante sku (añadida anteriormente a la lista) en el diccionario de stock
            if sku["SKU"] in ls_concidencia: #si hay coincidencias, se realiza el proceso de abajo
                cantidad = sku['cantidad'] #cambia la variable "cantidad", por la cantidad de stock que posee ese SKU en el diccionario stock
                contador = contador + cantidad #suma al contador la cantidad de stock correspondiente

        print(f"Total de stock para la marca {marca_busqueda}: {contador}")
    else:  # si no hay coincidencias, muestra el mensaje
        print("La marca no existe en el stock actual.")

    while True:  # permite repetir el proceso hasta que la respuesta del usuario sea correcta
        respuesta = input("¿Desea consultar el stock de otra marca? (SI/NO): ") 
        respuesta = respuesta.upper() #cambia la respuesta del usuario a mayusculas
        if respuesta == "SI":
            stock_marca()  # llama a la funcion stock_marca nuevamente
            break
        elif respuesta == "NO":
            menu()  # llama a la funcion menu nuevamente
            break
        else:
            print("Respuesta inválida, intente nuevamente.")

def busqueda_precios(): #Funcion que incializa la opcion 2 del menu

    ls_busqueda = [] #Inicializacion de una lista de busqueda
    ls_articulos=[] #Inicializacion de la lista final de articulos
    while True: #Permite realizar el proceso hasta que el valor ingresado sea entero
        try:
            precio_minimo = int(input("Ingrese precio mínimo: ")) #ingreso del precio minimo
            precio_maximo = int(input("Ingrese precio máximo: ")) #ingreso del precio maximo
            break
        except: #cualquier otro valor es invalido
            print("Debe ingresar valores enteros!!")

    for item in stock: # busca cualquier coincidencia segun los valores ingresados anteriormente
        if precio_minimo <= item["precio"] <= precio_maximo and item["cantidad"] > 0: #las coincidencias deben ser: Estar dentro del rango de precios y tener stock mayor a 0
            ls_busqueda.append(item["SKU"]) #añade a la lista de busqueda todos los SKU coincidentes con la busqueda

    for producto in productos: #busca coincidencias de la variable productos en el diccionario de productos
        if producto["SKU"] in ls_busqueda: #si hay coincidencias de SKU entre los de la lista anteriormente creada y los SKU del diccionario de productos, se hace el proceso de abajo
            articulo = producto["marca"] + "--" + producto["SKU"] #se crea el texto a mostrar al usuario, mostrando marca, guiones entre medio y el SKU al final almacenandolo en la variable articulo
            ls_articulos.append(articulo) #finalmente se añade la variable articulo en la lista de articulos final

    if ls_articulos: #si hay articulos en la lista de articulos, se realiza el proceso de abajo
        for articulo in ls_articulos: #por cada articulo en la lista, los muestra de forma verticar en formato "marca--sku"
            print (articulo)
        menu() #lanza la funcion menu nuevamente
    else: #si no hay articulos en la lista de articulos final, se realiza el proceso de abajo
        print("No hay notebooks en ese rango de precios.")
        respuesta = input("Deseas volver a consultar? (SI/NO): ") #pregunta si es que se quiere realizar el proceso nuevamente
        respuesta=respuesta.upper() #transforma la respuesta a mayusculas
        while True: #permite repetir el proceso hasta que se cumpla el si/no de la pregunta 
            if respuesta == "SI": #si la respuesta es si, lanza la funcion nuevamente
                busqueda_precios() #lanza la función busqueda_precios nuevamente
                break
            elif respuesta == "NO": #si la respuesta del usuario es no, vuelve al menu principal
                menu() #lanza la funcion menu nuevamente
                break
            else: #cualquier otra respuesta es invalida, debe ingresar obligatoriamente si/no
                print("Respuesta inválida, intente nuevamente")

def actualizar_precios (): #Funcion que inicializa la opción 3 del menu
    while True: #permite repetir el proceso hasta que se cumpla la respuesta correcta
        art_actualizar = input("Ingrese el SKU del producto a actualizar: ") #ingreso del usuario del precio del SKU a actualizar
        for articulo in stock: #busca en el diccionario de stock la variable articulo
            if articulo["SKU"] == art_actualizar: #si la variable articulo coincide con el SKU ingresado por el usuario, se realiza el proceso de abajo
                precio_actualizado = int(input("Ingrese el precio actualizado: ")) #solicita al usuario el precio actualizado el SKU ingresado
                articulo ["precio"] = precio_actualizado #actualiza el precio del SKU en el diccionario de stock
                print ("El precio del producto " + articulo["SKU"] + " fue actualizado a: " + str(articulo["precio"])) #muestra el SKU del producto y su nuevo precio
                break
        else: #si el SKU ingresado no existe, realiza el proceso de abajo
            print("El modelo no existe.")
        
        
        while True: #permite repetir el proceso hasta que se cumpla el si/no de la pregunta 
            respuesta = input ("¿Desea modificar el precio de otro modelo? (Si/No)").upper() #pregunta si quiere volver a realizar el proceso de cambio de precio, cambia la respuesta a mayuscula
            if respuesta == "SI": #si la respuesta es si, lanza la funcion nuevamente
                break
            elif respuesta == "NO": #si la respuesta del usuario es no, vuelve al menu principal
                menu() #lanza la funcion menu nuevamente
                return
            else: #cualquier otra respuesta es invalida, debe ingresar obligatoriamente si/no
                print("Respuesta inválida, intente nuevamente")



productos = [ #Diccionario de productos con caracteristicas
    {
        "SKU": "8475HD",
        "marca": "HP",
        "pantalla_pulgadas": 15.6,
        "ram": "8GB",
        "tipo_almacenamiento": "HDD",
        "capacidad_almacenamiento": "1TB",
        "procesador": "Intel Core i5",
        "tarjeta_grafica": "Nvidia GTX1050"
    },
    {
        "SKU": "2175HD",
        "marca": "LENOVO",
        "pantalla_pulgadas": 14,
        "ram": "4GB",
        "tipo_almacenamiento": "SSD",
        "capacidad_almacenamiento": "512GB",
        "procesador": "Intel Core i5",
        "tarjeta_grafica": "Nvidia GTX1050"
    },
    {
        "SKU": "JjfFHD",
        "marca": "ASUS",
        "pantalla_pulgadas": 14,
        "ram": "16GB",
        "tipo_almacenamiento": "SSD",
        "capacidad_almacenamiento": "256GB",
        "procesador": "Intel Core i7",
        "tarjeta_grafica": "Nvidia RTX2080Ti"
    },
    {
        "SKU": "fgdxFHD",
        "marca": "HP",
        "pantalla_pulgadas": 15.6,
        "ram": "8GB",
        "tipo_almacenamiento": "HDD",
        "capacidad_almacenamiento": "1TB",
        "procesador": "Intel Core i3",
        "tarjeta_grafica": "integrada"
    },
    {
        "SKU": "GF75HD",
        "marca": "ASUS",
        "pantalla_pulgadas": 15.6,
        "ram": "8GB",
        "tipo_almacenamiento": "HDD",
        "capacidad_almacenamiento": "1TB",
        "procesador": "Intel Core i7",
        "tarjeta_grafica": "Nvidia GTX1050"
    },
    {
        "SKU": "123FHD",
        "marca": "LENOVO",
        "pantalla_pulgadas": 14,
        "ram": "6GB",
        "tipo_almacenamiento": "HDD",
        "capacidad_almacenamiento": "1TB",
        "procesador": "AMD Ryzen 5",
        "tarjeta_grafica": "integrada"
    },
    {
        "SKU": "342FHD",
        "marca": "LENOVO",
        "pantalla_pulgadas": 15.6,
        "ram": "8GB",
        "tipo_almacenamiento": "HDD",
        "capacidad_almacenamiento": "1TB",
        "procesador": "AMD Ryzen 7",
        "tarjeta_grafica": "Nvidia GTX1050"
    },
    {
        "SKU": "UWU131HD",
        "marca": "DELL",
        "pantalla_pulgadas": 15.6,
        "ram": "8GB",
        "tipo_almacenamiento": "HDD",
        "capacidad_almacenamiento": "1TB",
        "procesador": "AMD Ryzen 3",
        "tarjeta_grafica": "Nvidia GTX1050"
    }
]
stock= [ #Diccionario de stock por SKU, con precio y cantidad
    {
        "SKU": "8475HD",
        "precio": 387990,
        "cantidad": 10
    },
    {
        "SKU": "2175HD",
        "precio": 327990,
        "cantidad": 4
    },
    {
        "SKU": "JjfFHD",
        "precio": 424990,
        "cantidad": 1
    },
    {
        "SKU": "fgdxFHD",
        "precio": 664990,
        "cantidad": 21
    },
    {
        "SKU": "123FHD",
        "precio": 290890,
        "cantidad": 32
    },
    {
        "SKU": "342FHD",
        "precio": 444990,
        "cantidad": 7
    },
    {
        "SKU": "GF75HD",
        "precio": 749990,
        "cantidad": 2
    },
    {
        "SKU": "UWU131HD",
        "precio": 349990,
        "cantidad": 1
    },
    {
        "SKU": "FS1230HD",
        "precio": 249990,
        "cantidad": 0
    }
]

def menu(): # Función que inicializa el menu
    print("Bienvenido a PyBooks") 
    print("***MENU PRINCIPAL***")
    print("1) Stock marca")
    print("2) Busqueda precios")
    print("3) Actualizar precios")
    print("4) Salir")
    seleccion=int(input("Ingrese una opción:")) 
    if seleccion == 1: # Seleccion 1, permite ingresar a la función de buscar el stock por marca
        stock_marca()
    elif seleccion == 2: # Selección 2, permite ingresar a la funcion de buscar articulos en un rango de precios
        busqueda_precios()
    elif seleccion == 3:# Selección 3, permite ingresar a la función de actualizar precios
        actualizar_precios()
    elif seleccion == 4:# Selección 4, permite salir del programa
        print ("El programa va a cerrarse ahora")
        return
    else:
        print("Opción inválida, seleccione nuevamente")
        menu() #Llama la función del menu nuevamente

menu ()   # Lanza la función "Menu" por primera vez             
          
            
         
            
            
