import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x380")
ventana.config(bg="white")

tk.Label(ventana, text="Primer numero:", bg="white").pack(pady=(15, 0))
entrada1= tk.Entry(ventana, font=("arial", 12), width=15)
entrada1.pack()

tk.Label(ventana, text="Segundo numero:", bg="white").pack(pady=(10, 0))
entrada2= tk.Entry(ventana, font=("arial", 12), width=15)
entrada2.pack()

resultado = tk.Label(ventana, text="Resultado:", font=("arial", 14), bg="white")
resultado.pack(pady=(20, 0))

def calcular(operacion):
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        if operacion == "suma":
            resultado.config(text=f"Resultado: {round(numero1 + numero2, 2)}")
        elif operacion == "resta":
            resultado.config(text=f"Resultado: {round(numero1 - numero2, 2)}")
        elif operacion == "multiplicacion":
            resultado.config(text=f"Resultado: {round(numero1 * numero2, 2)}")
        elif operacion == "division":
            if numero2 == 0:
                resultado.config(text="No se puede dividir por cero")
                return
            else:
                resultado.config(text=f"Resultado: {round(numero1 / numero2, 2)}")
    except ValueError:
        resultado.config(text="Escribre solo numeros")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text="Resultado:")


tk.Button(ventana, text="Sumar", width=10, command=lambda: calcular("suma")).pack(pady=(3,))
tk.Button(ventana, text="Restar", width=10, command=lambda: calcular("resta")).pack(pady=(3,))
tk.Button(ventana, text="Multiplicar", width=10, command=lambda: calcular("multiplicacion")).pack(pady=(3,))
tk.Button(ventana, text="Dividir", width=10, command=lambda: calcular("division")).pack(pady=(3,))
tk.Button(ventana, text="Limpiar", width=10, command=limpiar).pack(pady=(3,))

ventana.mainloop()