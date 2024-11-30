
import sqlite3

class VeterinariaBDD():
    
    def __init__(self):
        self._db_nombre = "veterinaria.db"
        self._conexion = None

    def AbrirConexion(self):
        self._conexion = sqlite3.connect(self._db_nombre)
        
    
    def CerrarConexion(self):
        
        if self._conexion:
            self._conexion.close()
    
    def EjecutarConsulta(self, consulta, parametros = None): # para las consultas que no devuelve ningun resultado (INSERT, UPDATE, DELETE)
        
        if parametros is None:
            parametros = []
        
        with self._conexion:
            cursor = self._conexion.cursor()
            cursor.execute(consulta, parametros)
            self._conexion.close()
        
    
    def LeerUno(self, consulta, parametros = None): # Lee sólo un resultado(el primer resultado coincidente) de la bdd
        
        if parametros is None:
            parametros = []
        
        cursor = self._conexion.cursor()
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone() # devuelve solo el primer resultado de la consulta, si no existe devuelve None
        
        return resultado
    
    def LeerTodos(self, consulta, parametros = None): # Lee todos los resultados(coincidentes) de la bdd
        
        if parametros is None:
            parametros = []

        cursor = self._conexion.cursor()
        cursor.execute(consulta, parametros)
        resultados = cursor.fetchall() # devuelve todos los resultados en una lista, si no existen resultados devuelve una lista vacia.

        return resultados

    def CrearTabla(self, nombre_tabla, columnas):
        pass
    
    if __name__ == "__main__":
        pass