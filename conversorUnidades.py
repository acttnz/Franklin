import tkinter as tk
from tkinter import messagebox

# Tasa de conversión 
Conversion = 514  

# realizar la conversión
def convertir():
    try:
        dolares = float(entrada_usd.get())
        # Convertir a colones (CRC)
        colones = dolares * Conversion
        colones = round(colones, 2)
        # Mostrar el resultado en la etiqueta de salida
        resultado_colones.config(text=f"{dolares} USD = {colones} CRC")
    except ValueError:
        # Si la entrada no es válida, mostrar un mensaje de error
        messagebox.showerror("Error", "Por favor ingrese un número válido.")

# limpiar campos
def limpiar():
    entrada_usd.delete(0, tk.END)
    resultado_colones.config(text="")

# ventana principal
def crear_ventana_principal():
    ventana = tk.Tk()
    ventana.title("Conversor de dolares a colones")
    ventana.geometry("450x250")
    return ventana

# widgets 
def crear_widgets(ventana):
    # Etiqueta para la entrada en USD
    ingresa_dolar =  tk.Label(ventana, text="Ingrese cantidad en USD:", 
                            font=("Arial", 12, "bold"),
                            fg="blue", bg="lightgray", padx=10, pady=10)
    ingresa_dolar.grid(row=0, column=0, padx=10, pady=10)

    # Entrada para el monto en USD
    global entrada_usd
    entrada_usd = tk.Entry(ventana, font=("Arial", 12), fg="black", bg="white", bd=5)
    entrada_usd.grid(row=0, column=1, padx=10, pady=10)

    # Botón para realizar la conversión
    boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
    boton_convertir.grid(row=1, column=0, padx=10, pady=10)

    # Botón para limpiar los campos
    boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
    boton_limpiar.grid(row=1, column=1, padx=10, pady=10)

    # Etiqueta para mostrar el resultado
    global resultado_colones
    resultado_colones = tk.Label(ventana, text="", 
                                  font=("Arial", 14, "italic"), fg="red", bg="white", 
                                  padx=10, pady=10)
    resultado_colones.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# verificación al cerrar
def cerrar_ventana():
    respuesta = messagebox.askyesno("Salir", "¿Seguro que desea cerrar la aplicación?")
    if respuesta:
        ventana.destroy()

# Iniciar la aplicación

ventana = crear_ventana_principal()
crear_widgets(ventana)

# Configurar la verificación al cerrar
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

ventana.mainloop()
