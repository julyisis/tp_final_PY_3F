
import tkinter as tk
from tkinter import ttk
from componentes.tk_componentes import*
from vistas.mascotas import vista_mascotas

"""


"""

def root():
    ventana = tk.Tk()
    ventana.title("Veterinaria")
    
    ventana.config(width=400, height=300)
    ventana.eval('tk::PlaceWindow %s center' % ventana.winfo_toplevel()) # centra la ventana 
    ventana.config(bg="#F0F8FF") 
    ventana.resizable(0,0)
    
    nombre_estilo_boton = "PrincipalEstiloButon.TButton"
    crear_estilo_estatico("boton_principal")
    
    nombre_estilo_titulo = "PrincipalEstiloLabel.TLabel"
    crear_estilo_estatico("titulo_principal")
    
    crear_titulo(ventana, "Sistema de Veterinaria", nombre_estilo_titulo)
    
    
    crear_boton(ventana,"Mascotas", 40, 100, nombre_estilo_boton, vista_mascotas)
    crear_boton(ventana, "Dueños", 160, 100, nombre_estilo_boton)
    crear_boton(ventana,"Visitas", 280, 100, nombre_estilo_boton)
    
    ventana.mainloop()