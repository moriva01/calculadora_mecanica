from modelo import *
from vista import *
from tkinter import messagebox

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.vista.btn_calcular.config(command=self.calcular_energia)#boton que ejecuta la funcion

    def calcular_energia(self):
        try:
            self.modelo.masa = float(self.vista.entry_masa.get())#pasa los datos que toma del la GUI
            self.modelo.altura = float(self.vista.entry_altura.get())
            self.modelo.velocidad = float(self.vista.entry_velocidad.get())

            self.modelo.calcular_energia()

            self.vista.label_energia_cinetica.config(text=f"Energía Cinética: {self.modelo.energia_cinetica:.2f} J")#lo actualiza retornando la funcion
            self.vista.label_energia_potencial.config(text=f"Energía Potencial: {self.modelo.energia_potencial:.2f} J")
            self.vista.label_energia_total.config(text=f"Energía Total: {self.modelo.energia_total:.2f} J")

            self.graficar_energia()

        except ValueError:
            messagebox.showerror("Error", "Por favor, introduzca valores numéricos válidos.")#si colocan datos invalidos

    def graficar_energia(self):#crea el grafico ps
        self.vista.grafico.clear()
        alturas = [0, self.modelo.altura / 2, self.modelo.altura]
        energias = [0, self.modelo.energia_total / 2, self.modelo.energia_total]
        self.vista.grafico.plot(alturas, energias, marker='o', linestyle='-')
        self.vista.grafico.set_xlabel('Altura (m)')
        self.vista.grafico.set_ylabel('Energía (J)')
        self.vista.grafico.set_title('Variación de la Energía con la Altura')
        self.vista.canvas.draw()

def main():#clase de inicializacion
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root)
    controlador = Controlador(modelo, vista)
    root.mainloop()

if __name__ == "__main__":#para retornar el main
    main()
