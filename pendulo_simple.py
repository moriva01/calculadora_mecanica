from paquetes import *

class PenduloSimpleCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_masa_pendulo = tk.Label(self, text="Masa (kg):")
        self.label_masa_pendulo.grid(row=0, column=0, padx=10, pady=5)
        self.entry_masa_pendulo = tk.Entry(self)
        self.entry_masa_pendulo.grid(row=0, column=1, padx=10, pady=5)

        self.label_longitud_cuerda_pendulo = tk.Label(self, text="Longitud de la Cuerda (m):")
        self.label_longitud_cuerda_pendulo.grid(row=1, column=0, padx=10, pady=5)
        self.entry_longitud_cuerda_pendulo = tk.Entry(self)
        self.entry_longitud_cuerda_pendulo.grid(row=1, column=1, padx=10, pady=5)

        self.label_angulo_pendulo = tk.Label(self, text="Ángulo (°):")
        self.label_angulo_pendulo.grid(row=2, column=0, padx=10, pady=5)
        self.entry_angulo_pendulo = tk.Entry(self)
        self.entry_angulo_pendulo.grid(row=2, column=1, padx=10, pady=5)

        self.calcular_button_pendulo = tk.Button(self, text="Calcular", command=self.calcular_energias_pendulo)
        self.calcular_button_pendulo.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.label_energia_cinetica_pendulo = tk.Label(self, text="Energía Cinética:")
        self.label_energia_cinetica_pendulo.grid(row=4, column=0, padx=10, pady=5)
        self.label_energia_cinetica_pendulo_resultado = tk.Label(self, text="")
        self.label_energia_cinetica_pendulo_resultado.grid(row=4, column=1, padx=10, pady=5)

        self.label_energia_potencial_pendulo = tk.Label(self, text="Energía Potencial:")
        self.label_energia_potencial_pendulo.grid(row=5, column=0, padx=10, pady=5)
        self.label_energia_potencial_pendulo_resultado = tk.Label(self, text="")
        self.label_energia_potencial_pendulo_resultado.grid(row=5, column=1, padx=10, pady=5)

        self.label_energia_mecanica_total_pendulo = tk.Label(self, text="Energía Mecánica Total:")
        self.label_energia_mecanica_total_pendulo.grid(row=6, column=0, padx=10, pady=5)
        self.label_energia_mecanica_total_pendulo_resultado = tk.Label(self, text="")
        self.label_energia_mecanica_total_pendulo_resultado.grid(row=6, column=1, padx=10, pady=5)

    def calcular_energias_pendulo(self):
        try:
            masa = float(self.entry_masa_pendulo.get())
            longitud_cuerda = float(self.entry_longitud_cuerda_pendulo.get())
            angulo = float(self.entry_angulo_pendulo.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos.")
            return

        energia_cinetica = 0.5 * masa * (2 * 9.81 * longitud_cuerda)
        energia_potencial = masa * 9.81 * longitud_cuerda * (1 - math.cos(math.radians(angulo)))
        energia_mecanica_total = energia_cinetica + energia_potencial

        self.label_energia_cinetica_pendulo_resultado.config(text=str(energia_cinetica))
        self.label_energia_potencial_pendulo_resultado.config(text=str(energia_potencial))
        self.label_energia_mecanica_total_pendulo_resultado.config(text=str(energia_mecanica_total))
