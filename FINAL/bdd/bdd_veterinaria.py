import sqlite3


def conectar_bd(nombre_bd):
    
    return sqlite3.connect(nombre_bd)

def cerrar_conexion(conexion):
    
    conexion.close()
    
def crear_tabla(conexion, consulta):
    
    
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        conexion.commit()
        cursor.close()
        print("Tabla creada exitosamente")
        
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
        return None
    

def insertar_datos(conexion, consulta, datos):
    
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, datos)
        conexion.commit()
        cursor.close()
        print("Datos cargados exitosamente")
        
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None
            
def leer_datos(conexion, consulta, parametros=()):
    
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, parametros)
        resultados = cursor.fetchall()
        cursor.close()
        
        return resultados

    except Exception as e:
        print(f"Error al leer los datos {e}")
        return None

def actualizar_datos(conexion, consulta, datos):
    
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, datos)
        conexion.commit()
        cursor.close()
        
        print("Datos actualizados correctamente")
        
    except Exception as e:
        print(f"Error al actualizar los datos {e}")
        return None

def eliminar_datos(conexion, consulta, parametros=()):
    
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, parametros)
        conexion.commit()
        cursor.close()
        
        print("Datos eliminados correctamente")
        
    except Exception as e:
        print(f"Error al eliminar los datos")
        
def ejecutar_consulta_segura(conexion, consulta, parametros=()):
    
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, parametros)
        conexion.commit()
        cursor.close()
            
        print("Consulta ejecutada exitosamente")
    
    except Exception as e:
        print(f"Error al ejecutar la consulta {e}")
    
if __name__ == "__main__":
    conexion = conectar_bd("veterinaria.db")
    
    consultasql_nueva_tabla = """
    CREATE TABLE IF NOT EXISTS Mascotas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especie TEXT NOT NULL,
        raza TEXT NOT NULL,
        edad INTEGER NOT NULL,
        estado TEXT NOT NULL
    );
    """
    # crear_tabla(conexion, consultasql_nueva_tabla)
    
    # insertar_datos(conexion, "INSERT INTO Mascotas (nombre, especie, raza, edad, estado) VALUES (?, ?, ?, ?, ?)", ("raul", "perro", "caniche", 4, "disponible"))

    mascotas = leer_datos(conexion, "SELECT * FROM Mascotas")
    print(mascotas)
    
    dueños = leer_datos(conexion, "SELECT * FROM dueños")
    print(dueños)
    
    actualizar_datos(conexion, "UPDATE Mascotas SET nombre = ? WHERE id_mascota = ?", ("Pipo", 1)) # actualiza un campo de un sólo registro
    #actualizar_datos(conexion, "UPDATE Mascotas SET nombre = ?, especie = ?, raza = ?, edad = ?, estado = ? WHERE id = ?",("Pedro", "gato", "aleman", 2, "no disponible",1)) # actualiza un registro completo
    
    mascotas = leer_datos(conexion, "SELECT * FROM Mascotas")
    print(mascotas)
    
    # eliminar_datos(conexion, "DELETE FROM Mascotas WHERE id_mascota = ?", (1,))
    
    eliminar_datos(conexion, "DELETE FROM Mascotas")
    mascotas = leer_datos(conexion, "SELECT * FROM Mascotas")
    print(mascotas)
    

    
    cerrar_conexion(conexion)