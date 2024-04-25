import tkinter as tk
from tkinter import messagebox

class CaidaLibreCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_masa_caida = tk.Label(self, text="Masa (kg):")
        self.label_masa_caida.grid(row=0, column=0, padx=10, pady=5)
        self.entry_masa_caida = tk.Entry(self)
        self.entry_masa_caida.grid(row=0, column=1, padx=10, pady=5)

        self.label_altura_caida = tk.Label(self, text="Altura (m):")
        self.label_altura_caida.grid(row=1, column=0, padx=10, pady=5)
        self.entry_altura_caida = tk.Entry(self)
        self.entry_altura_caida.grid(row=1, column=1, padx=10, pady=5)

        self.label_velocidad_caida = tk.Label(self, text="Velocidad (m/s):")
        self.label_velocidad_caida.grid(row=2, column=0, padx=10, pady=5)
        self.entry_velocidad_caida = tk.Entry(self)
        self.entry_velocidad_caida.grid(row=2, column=1, padx=10, pady=5)

        self.calcular_button_caida = tk.Button(self, text="Calcular", command=self.calcular_energias_caida)
        self.calcular_button_caida.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.label_energia_cinetica_caida = tk.Label(self, text="Energía Cinética:")
        self.label_energia_cinetica_caida.grid(row=4, column=0, padx=10, pady=5)
        self.label_energia_cinetica_caida_resultado = tk.Label(self, text="")
        self.label_energia_cinetica_caida_resultado.grid(row=4, column=1, padx=10, pady=5)

        self.label_energia_potencial_caida = tk.Label(self, text="Energía Potencial:")
        self.label_energia_potencial_caida.grid(row=5, column=0, padx=10, pady=5)
        self.label_energia_potencial_caida_resultado = tk.Label(self, text="")
        self.label_energia_potencial_caida_resultado.grid(row=5, column=1, padx=10, pady=5)

        self.label_energia_mecanica_total_caida = tk.Label(self, text="Energía Mecánica Total:")
        self.label_energia_mecanica_total_caida.grid(row=6, column=0, padx=10, pady=5)
        self.label_energia_mecanica_total_caida_resultado = tk.Label(self, text="")
        self.label_energia_mecanica_total_caida_resultado.grid(row=6, column=1, padx=10, pady=5)

    def calcular_energias_caida(self):
        try:
            masa = float(self.entry_masa_caida.get())
            altura = float(self.entry_altura_caida.get())
            velocidad = float(self.entry_velocidad_caida.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos.")
            return

        energia_cinetica = 0.5 * masa * velocidad ** 2
        energia_potencial = masa * 9.81 * altura
        energia_mecanica_total = energia_cinetica + energia_potencial

        self.label_energia_cinetica_caida_resultado.config(text=str(energia_cinetica))
        self.label_energia_potencial_caida_resultado.config(text=str(energia_potencial))
        self.label_energia_mecanica_total_caida_resultado.config(text=str(energia_mecanica_total))
