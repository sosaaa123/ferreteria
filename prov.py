#Aca hago un CRUD para la tabla proveedores
import sqlite3

conexion = sqlite3.connect("ferreteria.db")
cursor = conexion.cursor()

class proveedor:
    def __init__(self):
        pass

    def verProveedores(self):
        datos = ["Id", "Nombre", "Contacto", "Localidad"]
        res = cursor.execute("SELECT * FROM proveedores")
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

    
    def buscarProveedor(self, id_proveedor):
        datos = ["Id", "Nombre", "Contacto", "Localidad"]
        res = cursor.execute("SELECT * FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
        respuesta = res.fetchall()
        if respuesta:
            for item in respuesta:
                i = 0
                for dato in datos:
                    print(f"{dato}: {item[i]}")
                    i += 1
        else:
            print("\nProveedor no encontrado, id incorrecto.")

    def returnBusqueda(self, id_proveedor):
        res = cursor.execute("SELECT * FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
        respuesta = res.fetchall()
        return respuesta

    def ultId(self):
        res = cursor.execute("SELECT id_proveedor FROM proveedores ORDER BY id_proveedor DESC LIMIT 1") 
        respuesta = res.fetchall()
        return respuesta[0][0]


    def agregarProveedor(self, nombre, contacto, localidad):     
        cursor.execute("INSERT INTO proveedores (nombre, contacto, localidad) VALUES (?,?,?)", (nombre, contacto, localidad,))
        conexion.commit()
        nId = self.ultId()
        self.buscarProveedor(nId)
        print("\n¡Registro cargado exitosamente!")
        
        

    def borrarRegistro(self, id_proveedor):
        print("Vamos a borrar el siguiente registro: ")
        respuesta = self.returnBusqueda(id_proveedor)
        if respuesta:
            print("Proveedor encontrado")
            self.buscarProveedor(id_proveedor)
            answer = input("¿Desea borrarlo? S/N: ")
            if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
                cursor.execute("DELETE FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
                conexion.commit()
                print("¡Registro borrado exitosamente!")
            else:
                print("Operacion omitida")
        else:
            print("Proveedor no encontrado o id no existente, intente de nuevo.")

    def modificarRegistro(self, id_proveedor):
        resp = self.returnBusqueda(id_proveedor)
        if resp:
            while True: 
                print("Vamos a modificar este registro: ")
                self.buscarProveedor(id_proveedor)
                print("\nElija una opcion\n1)Para modificar nombre\n2)Para modificar contacto\n3)Para modificar localidad\n4)Para salir\n")
                opcion = input("")

                if opcion == "1":
                    nuevoValor = input("Vamos a modificar el nombre, porfavor ingrese el nuevo nombre: ")
                    cursor.execute("UPDATE proveedores SET nombre = ? WHERE id_proveedor = ?", (nuevoValor, id_proveedor))
                    conexion.commit()
                    print("Nombre modificado con exito!\n")
                    self.buscarProveedor(id_proveedor)



                elif opcion == "2":
                    nuevoValor = input("Vamos a modificar el contacto, porfavor ingrese el nuevo contacto: ")
                    cursor.execute("UPDATE proveedores SET contacto = ? WHERE id_proveedor = ?", (nuevoValor, id_proveedor))
                    conexion.commit()
                    print("Contacto modificado con exito")
                    self.buscarProveedor(id_proveedor)
    

                elif opcion == "3":
                    nuevoValor = input("Vamos a modificar la localidad, porfavor ingrese la nueva localidad: ")
                    cursor.execute("UPDATE proveedores SET localidad = ? WHERE id_proveedor = ?", (nuevoValor, id_proveedor))
                    conexion.commit()
                    print("Localidad modificada con exito")
                    self.buscarProveedor(id_proveedor)

                    opcion2 = input("Desea realizar otra operacion? S/N: ")

                elif opcion == "4":
                    print("///////////Saliendo////////////")
                    break


                else:
                    print("Ingrese una opcion valida porfavor.")
            
                opcion2 = input("Desea realizar otra operacion? S/N: ")
                if opcion2 == "N" or opcion2 == "n" or opcion2 == "no" or opcion2 == "No" or opcion2 == "NO":
                    print("¡Hasta pronto!")
                    break
        
        else:
            print("Proveedor no encontrado o id no existente, intente de nuevo")







        
        
        
        
                
