import tkinter as tk #importa GUI
from tkinter import ttk #importa notebooks de la GUI
from matplotlib.figure import Figure #para hacer graficas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #hacer las graficas en pestañas especificas

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("UR - Calculadora de Energía Mecánica")
        self.root.iconbitmap("logo.ico")

        # Crear Notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10, fill='both', expand=True)

        # Página de la calculadora
        self.frame_calculadora = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_calculadora, text='Calculadora')

        tk.Label(self.frame_calculadora, text="Masa (kg):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_masa = tk.Entry(self.frame_calculadora)
        self.entry_masa.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_calculadora, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_altura = tk.Entry(self.frame_calculadora)
        self.entry_altura.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_calculadora, text="Velocidad (m/s):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_velocidad = tk.Entry(self.frame_calculadora)
        self.entry_velocidad.grid(row=2, column=1, padx=5, pady=5)

        self.btn_calcular = tk.Button(self.frame_calculadora, text="Calcular Energía")
        self.btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

        self.frame_resultados = ttk.Frame(self.frame_calculadora)
        self.frame_resultados.grid(row=5, column=0, columnspan=2)

        tk.Label(self.frame_resultados, text="Resultados:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2)

        self.label_energia_cinetica = tk.Label(self.frame_resultados, text="")
        self.label_energia_cinetica.grid(row=1, column=0, columnspan=2)

        self.label_energia_potencial = tk.Label(self.frame_resultados, text="")
        self.label_energia_potencial.grid(row=2, column=0, columnspan=2)

        self.label_energia_termica = tk.Label(self.frame_resultados, text="")
        self.label_energia_termica.grid(row=3, column=0, columnspan=2)

        self.label_energia_total = tk.Label(self.frame_resultados, text="")
        self.label_energia_total.grid(row=4, column=0, columnspan=2)

        # Página de la gráfica
        self.frame_grafica = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_grafica, text='Gráfica')

        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.grafico = self.figura.add_subplot(111)
        self.grafico.set_xlabel('Altura (m)')
        self.grafico.set_ylabel('Energía (J)')
        self.grafico.set_title('Variación de la Energía con la Altura')

        self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame_grafica)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
