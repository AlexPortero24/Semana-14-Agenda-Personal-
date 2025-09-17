# La GUI se realizó con las indicaciones de la tarea
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Importar el DatePicker
from PIL import Image, \
    ImageTk  # Librería necesaria para redimensionar imágenes se requiere descargar la libreria Pillow.

print("Pillow funciona correctamente")

# crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal - Aplicación GUI")  # titulo descriptivo
ventana.geometry("700x500")  # son las dimensiones  de mi ventana
ventana.config(bg="khaki1")  # se añade color a la ventana
ventana.iconbitmap("sapo.ico") # se añade una imagen
ventana.resizable(False, False)  # Evita que la ventana sea redimensionable

# Imagen del sapo (más grande)
# ==========================
# Abrir la imagen y redimensionarla
# Imagen del sapo (más grande)
# ==========================
# Abrir la imagen y redimensionarla
imagen_sapo = Image.open("sapo1.png")  # Imagen con tema de Naruto(Anime)
imagen_sapo = imagen_sapo.resize((100, 100))  # Tamaño de la imagen
imagen_sapo_tk = ImageTk.PhotoImage(imagen_sapo)

# Mostrar la imagen en la ventana
label_sapo = tk.Label(ventana, image=imagen_sapo_tk, bg="khaki1")
label_sapo.place(x=10, y=290) # Aqui se cambia la ubicaion de mi imagen sapo1.png
# --------------------------------------------------------------------------------------

# Texto descriptivo arriba(Etiquetas)
# ==========================
label_texto = tk.Label(ventana, text="AGENDA PERSONAL - Ingrese información:",
                       font=("Arial", 14, "bold"), bg="aquamarine1", relief="solid")  # bg es el color de fondo
label_texto.place(x=150, y=20)

# ==========================
# TreeView para mostrar eventos (en lugar de Listbox)
# ==========================
frame_lista = tk.Frame(ventana, bg="khaki1")       # Crear cuadro con color
frame_lista.place(x=150, y=60, width=400, height=200)  # Posición y tamaño

arbol = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)  # Crear tabla

arbol.heading("Fecha", text="Fecha")              # Encabezado Fecha
arbol.heading("Hora", text="Hora")                # Encabezado Hora
arbol.heading("Descripción", text="Descripción") # Encabezado Descripción

arbol.column("Fecha", width=80)                   # Ancho columna Fecha
arbol.column("Hora", width=60)                    # Ancho columna Hora
arbol.column("Descripción", width=200)           # Ancho columna Descripción

arbol.pack(pady=5)                                # Mostrar tabla con espacio vertical

# ==========================
# Campos de entrada para la agenda
# ==========================
frame_campos = tk.Frame(ventana, bg="khaki1")        # Crear cuadro para los campos
frame_campos.place(x=150, y=270, width=400, height=100)  # Posición y tamaño del cuadro

# Campo de Fecha con etiqueta
label_fecha = tk.Label(frame_campos, text="Fecha:", bg="khaki1", font=("Arial", 10))  # Etiqueta "Fecha"
label_fecha.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Posición en fila 0, columna 0

# Selector de fecha (DatePicker)
date_picker = DateEntry(frame_campos,                         # Crear DateEntry dentro del cuadro
                        width=12,                              # Ancho del selector
                        background='darkblue',                 # Color de fondo
                        foreground='white',                    # Color del texto
                        borderwidth=2,                         # Ancho del borde
                        date_pattern='yyyy-mm-dd')             # Formato de fecha
date_picker.grid(row=0, column=1, padx=5, pady=5)             # Posición en fila 0, columna 1

# Campo de Hora
label_hora = tk.Label(frame_campos, text="Hora:", bg="khaki1", font=("Arial", 10))  # Etiqueta "Hora"
label_hora.grid(row=0, column=2, padx=5, pady=5, sticky="e")  # Posición en fila 0, columna 2

entry_hora = tk.Entry(frame_campos, width=10, font=("Arial", 10))  # Campo para ingresar hora
entry_hora.grid(row=0, column=3, padx=5, pady=5)  # Posición en fila 0, columna 3
entry_hora.insert(0, "12:00")  # Valor inicial por defecto

# Campo de Descripción
label_desc = tk.Label(frame_campos, text="Descripción:", bg="khaki1", font=("Arial", 10))  # Etiqueta "Descripción"
label_desc.grid(row=1, column=0, padx=5, pady=5, sticky="e")  # Posición en fila 1, columna 0

entry_desc = tk.Entry(frame_campos, width=30, font=("Arial", 10))  # Campo para ingresar descripción
entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we")  # Ocupa 3 columnas, se ajusta al ancho

# ==========================
# Funciones de botones ACTUALIZADAS para agenda
# ==========================
def agregar():
    fecha = date_picker.get()                    # Obtener fecha del selector
    hora = entry_hora.get().strip()              # Obtener hora del entry y quitar espacios
    descripcion = entry_desc.get().strip()       # Obtener descripción y quitar espacios

    if fecha and hora and descripcion:           # Verificar que todos los campos tengan valor
        arbol.insert("", "end", values=(fecha, hora, descripcion))  # Agregar fila a la tabla
        # Limpiar campos después de agregar
        entry_hora.delete(0, tk.END)            # Borrar hora del entry
        entry_desc.delete(0, tk.END)            # Borrar descripción del entry
        entry_hora.insert(0, "12:00")           # Resetear hora a "12:00"
        messagebox.showinfo("Éxito", "Evento agregado correctamente")  # Mostrar mensaje de éxito
    else:
        messagebox.showwarning("Advertencia", "Debe completar todos los campos.")  # Mensaje si faltan datos

# Función para eliminar evento seleccionado
def limpiar():
    seleccionado = arbol.selection()             # Obtener fila seleccionada
    if seleccionado:
        if messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?"):  # Confirmar eliminación
            arbol.delete(seleccionado)          # Borrar fila de la tabla
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")  # Mensaje si no hay selección

# Función para salir de la aplicación
def salir():
    if messagebox.askyesno("Salir", "¿Está seguro de que quiere salir?"):  # Confirmar salida
        ventana.quit()                            # Cerrar la ventana principal

# ==========================
# Botones, funciona llamando a la funcion agregar y limpiar al hacer clic
# ==========================
# Botón para agregar evento
btn_agregar = tk.Button(ventana, text="Agregar Evento", width=15, activebackground="cyan2", activeforeground="green",
                        command=agregar)  # Llama a la función agregar al hacer clic
btn_agregar.place(x=170, y=380)  # Posición del botón

# Botón para eliminar evento
btn_limpiar = tk.Button(ventana, text="Eliminar Evento", width=15, activebackground="cyan2", command=limpiar)  # Llama a limpiar
btn_limpiar.place(x=320, y=380)  # Posición del botón

# Botón para salir de la aplicación
btn_salir = tk.Button(ventana, text="Salir", width=15, activebackground="cyan2", command=salir)  # Llama a salir
btn_salir.place(x=470, y=380)  # Posición del botón

# Texto inferior informativo
label_info = tk.Label(ventana, text="Agenda Personal - Gestión de Eventos",
                      font=("Arial", 10), bg="khaki1", fg="blue")  # Etiqueta de información
label_info.place(x=150, y=440)  # Posición de la etiqueta

# su funcion es mantener la ventana abierta
ventana.mainloop()