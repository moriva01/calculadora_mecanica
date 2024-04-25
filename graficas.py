import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from caida_libre import CaidaLibreCalculator
from pendulo_simple import PenduloSimpleCalculator
from plano_inclinado import PlanoInclinadoCalculator

class Graficas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Caida Libre")
        self.tabControl.add(self.tab2, text="Péndulo Simple")
        self.tabControl.add(self.tab3, text="Plano Inclinado")

        self.tabControl.pack(expand=1, fill="both")

        # Add matplotlib canvas to each tab
        self.fig1 = plt.Figure(figsize=(5, 4), dpi=100)
        self.plot1 = self.fig1.add_subplot(111)
        self.canvas1 = FigureCanvasTkAgg(self.fig1, self.tab1)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.fig2 = plt.Figure(figsize=(5, 4), dpi=100)
        self.plot2 = self.fig2.add_subplot(111)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, self.tab2)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.fig3 = plt.Figure(figsize=(5, 4), dpi=100)
        self.plot3 = self.fig3.add_subplot(111)
        self.canvas3 = FigureCanvasTkAgg(self.fig3, self.tab3)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_caida_libre(self, masa, altura, velocidad):
        tiempo = np.linspace(0, 10, 100)
        posiciones = altura - 0.5 * 9.81 * tiempo**2
        self.plot1.plot(tiempo, posiciones, label='Posición')
        self.plot1.set_xlabel('Tiempo (s)')
        self.plot1.set_ylabel('Altura (m)')
        self.plot1.legend()
        self.canvas1.draw()

    def plot_pendulo_simple(self, masa, longitud_cuerda, angulo):
        tiempo = np.linspace(0, 10, 100)
        posiciones = longitud_cuerda * (1 - np.cos(np.radians(angulo)) * tiempo)
        self.plot2.plot(tiempo, posiciones, label='Posición')
        self.plot2.set_xlabel('Tiempo (s)')
        self.plot2.set_ylabel('Altura (m)')
        self.plot2.legend()
        self.canvas2.draw()

    def plot_plano_inclinado(self, masa, altura, velocidad, angulo):
        tiempo = np.linspace(0, 10, 100)
        posiciones = altura - 0.5 * 9.81 * (np.sin(np.radians(angulo)) * tiempo**2)
        self.plot3.plot(tiempo, posiciones, label='Posición')
        self.plot3.set_xlabel('Tiempo (s)')
        self.plot3.set_ylabel('Altura (m)')
        self.plot3.legend()
        self.canvas3.draw()
