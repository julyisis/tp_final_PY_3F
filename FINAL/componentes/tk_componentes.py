
import tkinter as tk
from tkinter import ttk


def crear_estilo_estatico(tipo: str):
    
    nuevo_estilo = ttk.Style()
    
    if tipo == "boton_principal":
        nuevo_estilo.configure(
        "PrincipalEstiloButon.TButton", 
        font=("Arial", 12, "bold"),          # Fuente del texto
                padding=5,                 # Espaciado interno del botón
                relief="rgroove",            # Estilo de relieve del botón
                width=10,                   # Ancho del botón
                anchor="center",            # Alineación del texto dentro del botón
                borderwidth=10,
                background="white",
                foreground= "darkgreen"
        )
    
    if tipo == "titulo_principal":
        nuevo_estilo.configure(
        "PrincipalEstiloLabel.TLabel",
        font=("Arial", 12, "bold"), 
                background="#F0F8FF",
                padding=5,
                foreground="black")
    
    if tipo == "titulo_seccion":
        nuevo_estilo.configure(
        "SeccionEstiloLabel.TLabel",
        font=("Arial", 25, "bold"), 
                background="#F0F8FF", 
                padding=5,
                foreground="black")


def crear_titulo(ventana: tk, nombre_titulo: str, nombre_estilo: str):
    
    
    nuevo_titulo = ttk.Label(ventana, text=nombre_titulo, style= nombre_estilo)
    
    ventana.update_idletasks() 
    ventana_ancho = ventana.winfo_width()
    ventana_alto = ventana.winfo_height()
    
    # Obtener las dimensiones del widget (Label)
    label_ancho = nuevo_titulo.winfo_width()
    label_alto = nuevo_titulo.winfo_height()
    posicion_y = (ventana_alto - label_alto) // 12
    
    if nombre_titulo == "Sistema de Veterinaria":
        posicion_x = (ventana_ancho - label_ancho) // 3.5
        
    elif nombre_titulo == "Mascotas":
        posicion_x = (ventana_ancho - label_ancho) // 2.6

    nuevo_titulo.place(x=posicion_x, y=posicion_y)

def crear_boton(ventana: tk, nombre_boton: str, posicion_x: int, posicion_y: int, nombre_estilo: str,funcion_a_ejecutar = None):
    
    nuevo_boton = ttk.Button(ventana, text=nombre_boton, style= nombre_estilo, command=funcion_a_ejecutar)
    nuevo_boton.place(x=posicion_x, y= posicion_y)
    
    


