import sqlite3
from prov import proveedor
from prod import productos
from ventas import ventas
conexion = sqlite3.connect("ferreteria.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS proveedores (id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, contacto TEXT, localidad TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS productos (id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio INTEGER, marca TEXT, stock INTEGER, id_proveedor, FOREIGN KEY (id_proveedor) REFERENCES proveedores (id_proveedor))")
cursor.execute("CREATE TABLE IF NOT EXISTS ventas (id_venta INTEGER PRIMARY KEY AUTOINCREMENT, cantidad INTEGER, id_producto, nombreProd TEXT ,total INTEGER, metPago TEXT, fecha TEXT, hora TEXT, FOREIGN KEY (id_producto) REFERENCES productos (id_producto))")

proveedorTable = proveedor()
productosTable = productos()
ventasTable = ventas()


opcion = True
while opcion:
    print("- Las tablas disponibles a consultar son:\n1)Para tabla Proveedores\n2)Para tabla productos\n3)Para tabla ventas\n4)Para salir")
    opcion = input("Ingrese una opcion: ")

    #Terminada
    if opcion == "1":
        opcion1 = ""
        while opcion1 != "6":
            print("- Las operaciones a realizar en la tabla proveedores son:\n1)Para ver proveedores\n2)Para buscar proveedor\n3)Para agregar proveedor\n4)Para modificar registro de un proveedor\n5)Para borrar un registro de proveedor\n6)Para salir")
            opcion1 = input("Ingrese una opcion: ")

            if opcion1 == "1":
                print("- Vamos a ver los registros de Proveedores -")
                proveedorTable.verProveedores()
                

            elif opcion1 == "2":
                print("- Vamos a buscar un proveedor por su id")
                value = input("Porfavor ingrese el id del proveedor que desea buscar: ")
                proveedorTable.buscarProveedor(value)


            elif opcion1 == "3":
                print("- Vamos a agregar un nuevo proveedor a la tabla ")
                nombre = input("Porfavor ingrese el nombre del nuevo proveedor: ")
                contacto = input(f"Porfavor ingrese el contacto del nuevo proveedoor: ")
                localidad = input(f"Porfavor ingrese la localidad del nuevo proveedor: ")
                proveedorTable.agregarProveedor(nombre,contacto,localidad)


            elif opcion1 == "4":
                print("-Vamos a modificar un registro de la tabla proveedores")
                value = input("porfavor ingrese el id del registro a modificar: ")
                proveedorTable.modificarRegistro(value)

            elif opcion1 == "5": 
                print("-Vamos a borrar el registro de un proveedor")
                value = input("Porfavor ingrese el id del proveedor a eliminar: ")
                proveedorTable.borrarRegistro(value)


            elif opcion1 == "6":
                print("Saliendo de la tabla proveedores...\n")
                opcion1 = "6"
                break

            else: 
                print("Ingrese una opcion validad, porfavor.")
            
            answer = input("Desea realizar otra operacion en proveedores? S/N: ")
            if answer == "N" or answer  == "n" or answer == "No" or answer == "no" or answer == "NO":
                print("Saliendo de la tabla proveedores...\n")
                opcion1 = "6"
                break

    #Terminada
    elif opcion == "2":
        opcion1 = ""
        while opcion1 != "8":
            print("- Las operaciones a realizar en la tabla productos son:\n1)Para ver productos\n2)Para buscar productos\n3)Para agregar producto\n4)Para modificar registro de producto\n5)Para borrar registro de producto\n6)Para ver los productos con stock menor a 10\n7)Para ver la suma total\n8)Para salir ")
            opcion1 = input("Ingrese una opcion: ")
            if opcion1 == "1":
                print("- Vamos a ver los registros de Productos -")
                productosTable.verProductos()

            elif opcion1 == "2":
                print("- Vamos a buscar productos")
                value = input("Porfavor ingrese el nombre del producto a buscar: ")
                value = value.capitalize()
                productosTable.buscarProducto(value)

            elif opcion1 == "3":
                print("- Vamos a agregar un nuevo producto a la tabla ")
                nombre = input("Porfavor ingrese el nombre del nuevo producto: ")
                nombre = nombre.capitalize()
                precio = input("Porfavor ingrese el precio del producto: ")
                marca = input("Porfavor ingrese la marca del producto: ")
                stock = input("Porfavor ingrese el numero de stock del producto: ")
                id_prov = input("Porfavor ingrese el id del proveedor del producto: ")
                productosTable.agregarProducto(nombre,precio,marca,stock, id_prov)


            elif opcion1 == "4":
                print("-Vamos a modificar un registro de la tabla productos")
                value = int(input("porfavor ingrese el id del registro del producto a modificar: "))
                productosTable.modificarRegistro(value)


            elif opcion1 == "5": 
                print("-Vamos a borrar el registro de un producto")
                value = input("Porfavor ingrese el id del producto a eliminar: ")
                productosTable.borrarRegistro(value)

            elif opcion1 == "6":
                productosTable.menorTen()

            elif opcion1 == "7":
                suma = productosTable.sumaTotal()
                print(f"La suma total de todos los productos si se vendieran seria: {suma}")

            elif opcion1 == "8":
                print("Saliendo de la tabla productos...\n")
                opcion1 = "8"
                break
            else: 
                print("Ingrese una opcion validad, porfavor.")
            
            answer = input("Desea realizar otra operacion en productos? S/N: ")
            if answer == "N" or answer  == "n" or answer == "No" or answer == "no" or answer == "NO":
                print("Saliendo de la tabla productos...\n")
                opcion1 = "8"
                break

    #Terminada
    elif opcion == "3":
        opcion1 = ""
        while opcion1 != "7":
            print("- Las operaciones a realizar en la tabla ventas son:\n1)Para ver ventas\n2)Para buscar venta\n3)Para agregar venta\n4)Para modificar registro de venta\n5)Para borrar registro de venta\n6)Para ver las ultimas 5 ventas\n7)Para salir")
            opcion1 = input("Ingrese una opcion: ")
            if opcion1 == "1":
                print("- Vamos a ver los registros de ventas -")
                ventasTable.verVentas()


            elif opcion1 == "2":
                print("- Vamos a buscar una venta")
                value = input("Porfavor ingrese el id de la venta a buscar: ")
                ventasTable.buscarVenta(value)
     

            elif opcion1 == "3":
                print("- Vamos a agregar una nueva venta a la tabla. ")
                idproducto = input("Porfavor ingrese el id del producto comprado: ")
                cantidad = int(input("Porfavor ingrese la cantidad comprada: "))
                metPago = input("Porfavor ingrese el metodo de pago: ")
                fecha = input("Porfavor ingrese la fecha de la venta: ")
                hora = input("Porfavor ingrese la hora de la venta: ")
                ventasTable.agregarVenta(cantidad, idproducto, metPago, fecha, hora)


            elif opcion1 == "4":
                print("-Vamos a modificar un registro de la tabla ventas.")
                value = input("porfavor ingrese el id del registro de venta a modificar: ")
                ventasTable.modificarVenta(value)



            elif opcion1 == "5": 
                print("-Vamos a borrar un registro de ventas")
                value = int(input("Porfavor ingrese el id del registro de venta a eliminar: "))
                ventasTable.borrarVenta(value)

            
            elif opcion1 == "6":
                ventasTable.mostraUlt5()

            elif opcion1 == "7":
                print("Saliendo de la tabla ventas...\n")
                opcion1 = "7"
                break

            else: 
                print("Ingrese una opcion validad, porfavor.")
            
            answer = input("Desea realizar otra operacion en ventas? S/N: ")
            if answer == "N" or answer  == "n" or answer == "No" or answer == "no" or answer == "NO":
                print("Saliendo de la tabla ventas...\n")
                opcion1 = "7"
                break

    elif opcion == "4":
        print("¡Hasta pronto!")
        opcion = False
    
    else:
        print("Porfavor ingrese una opcion valida.")









