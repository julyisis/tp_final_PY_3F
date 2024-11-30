import tkinter as tk
from tkinter import ttk
from componentes.tk_componentes import*

def vista_mascotas():
    
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Veterinaria")
    nueva_ventana.geometry("800x400")
    nueva_ventana.config(bg="#F0F8FF")
    nueva_ventana.resizable(0,0)
    nueva_ventana.update_idletasks() # asegura que las dimensiones de la ventana esten actualizadas

    pantalla_ancho = nueva_ventana.winfo_screenwidth()
    pantalla_alto = nueva_ventana.winfo_screenheight()
    ventana_ancho = nueva_ventana.winfo_width()
    ventana_alto = nueva_ventana.winfo_height()
    
    posicion_x = (pantalla_ancho - ventana_ancho) // 2
    posicion_y = (pantalla_alto - ventana_alto) // 2
    
    nueva_ventana.geometry(f'{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}')
    nombre_estilo_titulo = "SeccionEstiloLabel.TLabel"
    
    crear_estilo_estatico("titulo_seccion")
    crear_titulo(nueva_ventana, "Mascotas", nombre_estilo_titulo )
    
    nueva_ventana.grid_rowconfigure(0, weight=1)
    nueva_ventana.grid_rowconfigure(1, weight=1)
    nueva_ventana.grid_rowconfigure(2, weight=1)

    nueva_ventana.grid_columnconfigure(0, weight=1)
    nueva_ventana.grid_columnconfigure(1, weight=1)
    nueva_ventana.grid_columnconfigure(2, weight=1)
    
    nuevo_frame = tk.Frame(nueva_ventana, width=600, height=200)
    nuevo_frame.grid(row=1, column=1, padx=10, pady=10)
    nuevo_frame.grid_propagate(False) 
    
    tree = ttk.Treeview(nuevo_frame, columns=("id_mascota", "id_dueño","nombre", "especie", "raza", "estado"), show="headings")
    
    tree.column("id_mascota", width=12, minwidth=6)  
    tree.column("id_dueño", width=12, minwidth=6)  
    tree.column("nombre", width=50, minwidth=25)  
    tree.column("especie", width=25, minwidth=12)
    tree.column("raza", width=25, minwidth=12)
    tree.column("estado", width=25, minwidth=12)
    
    tree.heading("id_mascota", text="ID")
    tree.heading("id_dueño", text="Dueño")
    tree.heading("nombre", text="Nombre")
    tree.heading("especie", text="Especie")
    tree.heading("raza", text="Raza")
    tree.heading("estado", text="Estado")
    
    # Configuración de colores para filas intercaladas
    tree.tag_configure('even', background='#f0f0f0')  # Color para filas pares
    tree.tag_configure('odd', background='#ffffff')   # Color para filas impares
    
    tree.grid(row=0, column=0, sticky="nsew")

    scroll_y = ttk.Scrollbar(nuevo_frame, orient=tk.VERTICAL, command=tree.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")  # Colocar la barra de desplazamiento a la derecha
    tree.configure(yscrollcommand=scroll_y.set)

    # Ajustar el Frame para que se expanda en ambas direcciones (fácil redimensionamiento)
    nuevo_frame.grid_rowconfigure(0, weight=1)
    nuevo_frame.grid_columnconfigure(0, weight=1)