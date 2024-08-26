#Aca hago un CRUD para la tabla productos
import sqlite3
from prov import proveedor
proveedorTable = proveedor()
conexion = sqlite3.connect("ferreteria.db")
cursor = conexion.cursor()



class productos:

    def __init__(self):
        pass

    def verProductos(self):
        datos = ["Id","Nombre", "Precio", "Marca", "Stock", "Id del proveedor"]
        res = cursor.execute("SELECT * FROM productos")
        respuesta = res.fetchall()
        y = 0
        for item in respuesta:
            y += 1
            i = 0
            print(f"-Producto {y}")
            for dato in datos:
                print(f"{dato}: {item[i]}")
                i += 1  
            print("\n")
    
    def ver_por_id(self, id_producto):
        datos = ["Id","Nombre", "Precio", "Marca", "Stock", "Id del proveedor"]
        res = cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
        respuesta = res.fetchall()
        y = 0
        if respuesta:
            for item in respuesta:
                y+= 1
                i = 0
                for dato in datos:
                    print(f"{dato}: {item[i]}")
                    i += 1
                print("\n")
        else:
                print("Producto no encontrado por id, intente de nuevo.")


    def buscarProducto(self, producto):
        datos = ["Id","Nombre", "Precio", "Marca", "Stock", "Id del proveedor"]
        res = cursor.execute("SELECT * FROM productos WHERE nombre = ?", (producto,))
        respuesta = res.fetchall()
        y = 0
        if respuesta:
            print("Productos encontrados: ")
            for item in respuesta:
                y+= 1
                i = 0
                for dato in datos:
                    print(f"{dato}: {item[i]}")
                    i += 1  
                print("\n")
        else:
            print("Productos no encontrados o no existentes, intente de nuevo")

    def agregarProducto(self, nombre, precio, marca, stock, id_proveedor): 
        res = proveedorTable.returnBusqueda(id_proveedor)
        if res:  
            cursor.execute("INSERT INTO productos (nombre, precio, marca, stock, id_proveedor) VALUES (?,?,?,?,?)", (nombre, precio, marca, stock, id_proveedor))
            conexion.commit()
            print("¡Registro cargado exitosamente!")
        else:
            print("Proveedor no encontrado o no existente, intente de nuevo.")
        

    def borrarRegistro(self, id_producto):
        resp = self.returnBusqueda(id_producto)
        if resp:
            print("Vamos a borrar el siguiente registro: ")
            self.ver_por_id(id_producto)
            answer = input("¿Desea borrarlo? S/N: ")
            if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
                cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
                conexion.commit()
                print("¡Registro borrado exitosamente!")
            else:
                print("Operacion omitida")
        else:
            print("El id ingresado no corresponde no coincide con ningun producto o no fue encontrado, intente de nuevo.")

    def returnBusqueda(self, id_producto):
            res = cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
            respuesta = res.fetchall()
            return respuesta

    def modificarRegistro(self, id_producto):
        resp = self.returnBusqueda(id_producto)
        if resp:
            print("Vamos a modificar este registro: ")
            self.ver_por_id(id_producto)
            print("Elija una opcion\n1)Para modificar nombre\n2)Para modificar precio\n3)Para modificar marca\n4)Para modificar numero de stock\n5)Para modificar proveedor\n6)Para salir\n")
            opcion = input("")
            while True:
                if opcion == "1":
                    nuevoValor = input("Vamos a modificar el nombre, porfavor ingrese el nuevo nombre: ")
                    nuevoValor = nuevoValor.capitalize()
                    cursor.execute("UPDATE productos SET nombre = ? WHERE id_producto = ?", (nuevoValor, id_producto))
                    conexion.commit()
                    print("Nombre modificado con exito!\n")
                    self.ver_por_id(id_producto)

                elif opcion == "2":
                    nuevoValor = input("Vamos a modificar el precio, porfavor ingrese el nuevo precio: ")
                    cursor.execute("UPDATE productos SET precio = ? WHERE id_producto = ?", (nuevoValor, id_producto))
                    conexion.commit()
                    print("Precio modificado con exito")
                    self.ver_por_id(id_producto)

                elif opcion == "3":
                    nuevoValor = input("Vamos a modificar la marca, porfavor ingrese la nueva marca: ")
                    cursor.execute("UPDATE productos SET marca = ? WHERE id_producto = ?", (nuevoValor, id_producto))
                    conexion.commit()
                    self.ver_por_id(id_producto)
                    print("Marca modificada con exito")

                elif opcion == "4":
                    nuevoValor = input("Vamos a modificar el numero de stock, porfavor ingrese el nuevo numero: ")
                    cursor.execute("UPDATE productos SET stock = ? WHERE id_producto = ?", (nuevoValor, id_producto))
                    conexion.commit()
                    self.ver_por_id(id_producto)
                    print("Numero de stock modificado con exito")
                
                elif opcion == "5":
                    nuevoValor = input("Vamos a modificar el proveedor, porfavor ingrese el id del nuevo proveedor: ")
                    respp = proveedorTable.returnBusqueda(nuevoValor)
                    if respp:
                        proveedorTable.buscarProveedor(nuevoValor)
                        print("El id coincide con el siguiente proveedor, es correcto?")
                        answer = input("S/N: ")
                        if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
                            cursor.execute("UPDATE productos SET id_proveedor = ? WHERE id_producto = ?", (nuevoValor, id_producto))
                            conexion.commit()
                            self.ver_por_id(id_producto)
                            print("Proveedor modificado con exito")
                    else:
                        print("El id ingresado no coincide con ningun proveedor o no ue encontrado, intente de nuevo")
                
                elif opcion == "6":
                    print("///////////Saliendo////////////")
                    break

                else:
                    print("Ingrese una opcion valida porfavor.")
            

                print("Elija una opcion\n1)Para modificar nombre\n2)Para modificar precio\n3)Para modificar marca\n4)Para modificar numero de stock\n5)Para modificar proveedor\n6)Para salir\n")
                opcion = input("")

        else:
            print("Producto no encontrado o id no existente, porfavor intente de nuevo")

    #Esto es una chantada, pero ya fue

    def verPrecio(self, id_producto):
        res = cursor.execute("SELECT precio FROM productos WHERE id_producto = ?", (id_producto,))
        respuesta = res.fetchall()
        precio = []
        for item in respuesta:
            precio.append(item)
        return precio[0][0]

    def verNombre(self, id_producto):
        res = cursor.execute("SELECT nombre FROM productos WHERE id_producto = ?", (id_producto,))
        respuesta = res.fetchall()
        nombre = []
        for item in respuesta:
            nombre.append(item)
        
        return nombre[0][0]

    def reStock(self, id_producto, nstock):
        cursor.execute("UPDATE productos SET stock = stock - ? WHERE id_producto = ?", (nstock, id_producto))
        conexion.commit()

    def maStock(self, id_producto, nstock):
        cursor.execute("UPDATE productos SET stock = stock + ? WHERE id_producto = ?", (nstock, id_producto))
        conexion.commit()



    """Mostrar todos los productos con cantidad menor  10"""

    def menorTen(self):
        datos = ["Id","Nombre", "Precio", "Marca", "Stock", "Id del proveedor"]
        res = cursor.execute("SELECT * FROM productos WHERE stock < 10")
        respuesta = res.fetchall()
        y = 0
        print("-Los productos con stock menor a 10 son:")
        for item in respuesta:
            y += 1
            i = 0
            print(f"-Producto {y}")
            for dato in datos:
                print(f"{dato}: {item[i]}")
                i += 1  
            print("\n")

    """Mostrar el valor total de todos los productos de inventario"""
    def sumaTotal(self):
        res = cursor.execute("SELECT precio FROM productos")
        respuesta = res.fetchall()   
        suma = 0 
        for item in respuesta:
            suma = suma + item[0]
        

        res1 = cursor.execute("SELECT stock FROM productos")
        respuesta1 = res1.fetchall()
        suma1 = 0

        for item in respuesta1:
            suma1 = suma1 + item[0]

        return suma*suma1

    
        
        


    

    