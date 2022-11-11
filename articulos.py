import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="127.0.0.1", 
                                              user="root", 
                                              passwd="", 
                                              database="centro_comercial")
        return conexion


    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT valor, stock FROM electrodomestico WHERE producto=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT producto, valor, stock FROM electrodomestico"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update electrodomestico set stock=%s where producto=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount 

        