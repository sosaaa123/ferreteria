import sqlite3
from prod import productos
productosTable = productos()
conexion = sqlite3.connect("ferreteria.db")
cursor = conexion.cursor()

class ventas:
    def __init__(self):
        pass

    def verVentas(self):
        datos = ["Id","Cantidad","IdProducto", "Producto", "Total", "Metodo de pago", "Fecha", "Hora"]
        res = cursor.execute("SELECT * FROM ventas")
        respuesta = res.fetchall()
        y = 0
        for item in respuesta:
            y += 1
            i = 0
            print(f"-Registro {y}")
            for dato in datos:
                print(f"{dato}: {item[i]}")
                i += 1  
            print("\n")   
    
    def buscarVenta(self, id_venta):
        resp = self.returnBusqueda(id_venta)
        datos = ["Id","Cantidad","IdProducto", "Producto", "Total", "Metodo de pago", "Fecha", "Hora"]
        res = cursor.execute("SELECT * FROM ventas WHERE id_venta = ?", (id_venta,))
        respuesta = res.fetchall()
        y = 0
        if resp:
            for item in respuesta:
                y += 1
                i = 0
                print(f"-Venta encontrada")
                for dato in datos:
                    print(f"{dato}: {item[i]}")
                    i += 1  
                print("\n")
        else:
            print("Id ingresado no correspondiente a ninguna venta o no encontrado, porfavor intente de vuelta.")

    def returnBusqueda(self, id_venta):
            res = cursor.execute("SELECT * FROM ventas WHERE id_venta = ?", (id_venta,))
            respuesta = res.fetchall()
            return respuesta

    def ultId(self):
        res = cursor.execute("SELECT id_venta FROM ventas ORDER BY id_venta DESC LIMIT 1") 
        respuesta = res.fetchall()
        return respuesta[0][0]

    def agregarVenta(self, cantidad, id_producto, metPago, fecha, hora): 
        resp = productosTable.returnBusqueda(id_producto)
        if resp:
            nombreProd = productosTable.verNombre(id_producto)
            precio = productosTable.verPrecio(id_producto) 
            total = precio*cantidad  
            productosTable.reStock(id_producto, cantidad)
            cursor.execute("INSERT INTO ventas (cantidad, id_producto, nombreProd, total, metPago, fecha, hora) VALUES (?,?,?,?,?,?,?)", (cantidad, id_producto, nombreProd, total, metPago, fecha, hora,))
            conexion.commit()
            print("¡Registro cargado exitosamente!")
            u  = self.ultId()
            self.buscarVenta(u)
        else:
            print("Fallo al cargar registro, Id de venta no encontrado o no correspondiente a ningun registro en ventas, intente de vuelta.")


    #   Aca otra chantada mas
    def verCantidad(self, id_venta):
        res = cursor.execute("SELECT cantidad FROM ventas WHERE id_venta = ?", (id_venta,))
        respuesta = res.fetchall()
        cant = []
        for item in respuesta:
            cant.append(item)
        return cant[0][0]

    def verIdProd(self, id_venta):
        res = cursor.execute("SELECT id_producto FROM ventas WHERE id_venta = ?", (id_venta,))
        respuesta = res.fetchall()
        aidProducto = []
        for item in respuesta:
            aidProducto.append(item)
        return aidProducto[0][0]

    def returnIdprodVenta(self, id_venta):
        res = cursor.execute("SELECT id_producto FROM ventas WHERE id_venta = ?", (id_venta,))
        respuesta = res.fetchall()
        cant = []
        for item in respuesta:
            cant.append(item)
        return cant[0][0]

    def modificarVenta(self, id_venta):
        resp = self.returnBusqueda(id_venta)
        if resp:
            print("Vamos a modificar este registro: ")
            self.buscarVenta(id_venta)
            print("Elija una opcion\n1)Para modificar el producto vendido\n2)Para modificar la cantidad\n3)Para modificar el metodo de pago\n4)Para modificar la fecha\n5)Para modificar la hora\n6)Para salir")
            opcion = input("")

            while True:

                if opcion == "1":
                    prodViejo = self.verIdProd(id_venta)
                    nuevoValor = input("Vamos a modificar el producto vendido en la venta, porfavor ingrese el id del producto a ingresar en la venta: ")
                    print("Producto encontrado:")
                    productosTable.ver_por_id(nuevoValor)
                    answer = input("Desea modificar la venta por este producto? S/N: ")
                    if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
                        nombreProd = productosTable.verNombre(nuevoValor)
                        precio = productosTable.verPrecio(nuevoValor) 
                        cantidad = self.verCantidad(id_venta)
                        total = precio  * cantidad 
                        productosTable.maStock(prodViejo, cantidad)
                        productosTable.reStock(nuevoValor,cantidad)
                        cursor.execute("UPDATE ventas SET id_producto = ?, nombreProd = ?, total = ?  WHERE id_venta = ?", (nuevoValor, nombreProd, total,  id_venta))
                        conexion.commit()
                        print("Venta modificada con exito, tambien se han cambiado los valores del precio y la cantidad\n")
                        self.buscarVenta(id_venta)


                elif opcion == "2":
                    nuevoValor = int(input("Vamos a modificar la cantidad, porfavor ingrese la nueva cantidad: "))
                    idprod = self.returnIdprodVenta(id_venta)
                    cantidadVieja = self.verCantidad(id_venta)
                    diferencia = cantidadVieja - nuevoValor
                    productosTable.maStock(idprod,diferencia)
                    precio = productosTable.verPrecio(idprod)
                    total = precio * nuevoValor
                    cursor.execute("UPDATE ventas SET cantidad = ?, total = ? WHERE id_venta = ?", (nuevoValor, total, id_venta))
                    conexion.commit()
                    print("Cantidad y precio modificado con exito!")
                    self.buscarVenta(id_venta)
    

                elif opcion == "3":
                    nuevoValor = input("Vamos el metodo de pago, porfavor ingrese el nuevo metodo de pago de la venta: ")
                    cursor.execute("UPDATE ventas SET metPago = ? WHERE id_venta = ?", (nuevoValor, id_venta))
                    conexion.commit()
                    print("metodo de pago modificado con exito")
                    self.buscarVenta(id_venta)

            
                elif opcion == "4":
                    nuevoValor = input("Vamos la fecha de la venta, porfavor ingrese la nueva fecha: ")
                    cursor.execute("UPDATE ventas SET fecha = ? WHERE id_venta = ?", (nuevoValor, id_venta))
                    conexion.commit()
                    print("fecha de la venta modificada con exito!")
                    self.buscarVenta(id_venta)


                elif opcion == "5":
                    nuevoValor = input("Vamos la hora de la venta, porfavor ingrese la nueva hora: ")
                    cursor.execute("UPDATE ventas SET hora = ? WHERE id_venta = ?", (nuevoValor, id_venta))
                    conexion.commit()
                    print("hora de la venta modificada con exito!")
                    self.buscarVenta(id_venta)

                elif opcion == "6":
                    print("///////////Saliendo////////////")
                    break


                else:
                    print("Ingrese una opcion valida porfavor.")
            
            
                print("Elija una opcion\n1)Para modificar el producto vendido\n2)Para modificar la cantidad\n3)Para modificar el metodo de pago\n4)Para modificar la fecha\n5)Para modificar la hora\n6)Para salir")
                opcion = input("")

        else:
            print("El id ingresado no coincide con ninguna venta o no fue encontrado, intente de nuevo")    

            

    def borrarVenta(self, id_venta):
        respp = self.returnBusqueda(id_venta)
        if respp:
            print("El registro a eliminar es el siguiente")
            self.buscarVenta(id_venta)
            answer = input("¿Desea borrarlo? S/N: ")
            if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
                res = cursor.execute("SELECT id_venta FROM ventas ORDER BY id_venta DESC LIMIT 3")
                respuesta = res.fetchall()
                for item in respuesta:
                    if id_venta == item[0]:
                        cantidad = self.verCantidad(id_venta)
                        idProd = self.returnIdprodVenta(id_venta)
                        productosTable.maStock(idProd,cantidad)
                        cursor.execute("DELETE FROM ventas WHERE id_venta = ?", (id_venta,))
                        conexion.commit()
                        print("Registro borrado exitosamente.")
                    
                        
        else:
            print("El id ingresado no corresponde a ninguna venta, no fue encontrado o no corresponde a los ultimos tres registros, intente de vuelta")



    def mostraUlt5(self):
        res = cursor.execute("SELECT * FROM ventas ORDER BY id_venta DESC LIMIT 5") 
        respuesta = res.fetchall()
        datos = ["Id","Cantidad","IdProducto", "Producto", "Total", "Metodo de pago", "Fecha", "Hora"]
        y = 0
        print("-Las ultimas 5 ventas fueron:")
        for item in respuesta:
            y += 1
            i = 0
            print(f"-Registro {y}")
            for dato in datos:
                print(f"{dato}: {item[i]}")
                i += 1  
            print("\n")   

