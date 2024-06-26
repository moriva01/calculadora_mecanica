from paquetes import *

class PlanoInclinadoCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_masa_plano = tk.Label(self, text="Masa (kg):")
        self.label_masa_plano.grid(row=0, column=0, padx=10, pady=5)
        self.entry_masa_plano = tk.Entry(self)
        self.entry_masa_plano.grid(row=0, column=1, padx=10, pady=5)

        self.label_altura_plano = tk.Label(self, text="Altura (m):")
        self.label_altura_plano.grid(row=1, column=0, padx=10, pady=5)
        self.entry_altura_plano = tk.Entry(self)
        self.entry_altura_plano.grid(row=1, column=1, padx=10, pady=5)

        self.label_velocidad_plano = tk.Label(self, text="Velocidad (m/s):")
        self.label_velocidad_plano.grid(row=2, column=0, padx=10, pady=5)
        self.entry_velocidad_plano = tk.Entry(self)
        self.entry_velocidad_plano.grid(row=2, column=1, padx=10, pady=5)

        self.label_grado_inclinacion_plano = tk.Label(self, text="Grado de Inclinación (°):")
        self.label_grado_inclinacion_plano.grid(row=3, column=0, padx=10, pady=5)
        self.entry_grado_inclinacion_plano = tk.Entry(self)
        self.entry_grado_inclinacion_plano.grid(row=3, column=1, padx=10, pady=5)

        self.calcular_button_plano = tk.Button(self, text="Calcular", command=self.calcular_energias_plano)
        self.calcular_button_plano.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.label_energia_cinetica_plano = tk.Label(self, text="Energía Cinética:")
        self.label_energia_cinetica_plano.grid(row=5, column=0, padx=10, pady=5)
        self.label_energia_cinetica_plano_resultado = tk.Label(self, text="")
        self.label_energia_cinetica_plano_resultado.grid(row=5, column=1, padx=10, pady=5)

        self.label_energia_potencial_plano = tk.Label(self, text="Energía Potencial:")
        self.label_energia_potencial_plano.grid(row=6, column=0, padx=10, pady=5)
        self.label_energia_potencial_plano_resultado = tk.Label(self, text="")
        self.label_energia_potencial_plano_resultado.grid(row=6, column=1, padx=10, pady=5)

        self.label_energia_mecanica_total_plano = tk.Label(self, text="Energía Mecánica Total:")
        self.label_energia_mecanica_total_plano.grid(row=7, column=0, padx=10, pady=5)
        self.label_energia_mecanica_total_plano_resultado = tk.Label(self, text="")
        self.label_energia_mecanica_total_plano_resultado.grid(row=7, column=1, padx=10, pady=5)

    def calcular_energias_plano(self):
        try:
            masa = float(self.entry_masa_plano.get())
            altura = float(self.entry_altura_plano.get())
            velocidad = float(self.entry_velocidad_plano.get())
            grado_inclinacion = math.radians(float(self.entry_grado_inclinacion_plano.get()))
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos.")
            return

        energia_cinetica = 0.5 * masa * velocidad ** 2
        energia_potencial = masa * 9.81 * altura * math.sin(grado_inclinacion)
        energia_mecanica_total = energia_cinetica + energia_potencial

        self.label_energia_cinetica_plano_resultado.config(text=str(energia_cinetica))
        self.label_energia_potencial_plano_resultado.config(text=str(energia_potencial))
        self.label_energia_mecanica_total_plano_resultado.config(text=str(energia_mecanica_total))
