import tkinter as tk
from tkinter import ttk
from caida_libre import CaidaLibreCalculator
from pendulo_simple import PenduloSimpleCalculator
from plano_inclinado import PlanoInclinadoCalculator
from graficas import Graficas

def main():
    root = tk.Tk()
    root.title("UR - Calculadora de Energía Mecánica")
    root.iconbitmap("logo.ico")

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text="Caida Libre")
    caida_libre_calculator = CaidaLibreCalculator(tab1)

    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text="Péndulo Simple")
    pendulo_simple_calculator = PenduloSimpleCalculator(tab2)

    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text="Plano Inclinado")
    plano_inclinado_calculator = PlanoInclinadoCalculator(tab3)

    tab4 = ttk.Frame(tab_control)
    tab_control.add(tab4, text="Gráficas")
    graficas = Graficas(tab4)
    graficas.plot_caida_libre(10, 20, 0)  # Ejemplo de gráfico para caída libre
    graficas.plot_pendulo_simple(10, 5, 30)  # Ejemplo de gráfico para péndulo simple
    graficas.plot_plano_inclinado(10, 20, 0, 30)  # Ejemplo de gráfico para plano inclinado

    tab_control.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
