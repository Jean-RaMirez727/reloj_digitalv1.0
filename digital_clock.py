import tkinter as tk
from time import strftime

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #setting title
        self.title("Reloj Digital")
        self.configure(bg="black")
        #setting window size
        width = 800
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=15)
        self.rowconfigure([1,2], weight=1)
        self.minsize(width=380, height=170)
        self.iconbitmap("4305432.ico")
        
        self.widgets()
        
        self.update_clock()
        
    def update_clock(self):
        
        current_time = strftime('%H:%M:%S')
        dia = strftime('%A')
        fecha = strftime('%d - %m - %y')
        
        if dia == 'Monday':
            dia = 'Lunes'
        elif dia == 'Tuesday':
            dia = 'Martes'
        elif dia == 'Wednesday':
            dia = 'Miercoles'
        elif dia == 'Thursday':
            dia = 'Jueves'
        elif dia == 'Friday':
            dia = 'Viernes'
        elif dia == 'Saturday':
            dia = 'Sábado'
        elif dia == 'Sunday':
            dia = 'Domingo'
        
        self.label.configure(text=current_time)
        self.dia_semana.configure(text=dia)
        self.fecha.configure(text=fecha)
        self.after(1000, self.update_clock)
        
    def ancho_texto(self, event):
        font_size = int(event.width / 5)
    # Configurar el nuevo tamaño de fuente en la etiqueta
        self.label.configure(font=("DS-Digital", font_size, "bold"), fg="#00ffff", bg="black")
        
    def ancho_texto2(self, event):
        font_size = int(event.width / 20)
    # Configurar el nuevo tamaño de fuente en la etiqueta
        self.dia_semana.configure(font=("Robot Crush", font_size), fg="#00ffff", bg="black")
        self.fecha.configure(font=("Robot Crush", font_size,), fg="#00ffff", bg="black")
        
    def widgets(self):
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=0, column=0, sticky="nsew") #
        
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)

        self.label = tk.Label(self.frame1, text="")
        self.label.grid(row=0, column=0, sticky='nsew')  # Sticky para que la etiqueta se expanda en todas las direcciones
        
        self.frame2 = tk.Frame(self, bg="#000")
        self.frame2.grid(row=1, column=0, sticky="nsew") #
        
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        
        self.dia_semana = tk.Label(self.frame2, text="")
        self.dia_semana.grid(row=1, column=0, sticky="nsew") # dia semana
        
        self.frame3 = tk.Frame(self)
        self.frame3.grid(row=2, column=0, sticky="nsew") #
        
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        
        self.fecha = tk.Label(self.frame3, text="")
        self.fecha.grid(row=0, column=0, sticky="nsew") # fecha
        
        self.frame4 = tk.Frame(self, bg="#000", height=25)
        self.frame4.grid(row=3, column=0, sticky="nsew") #
        
        self.bind("<Configure>", lambda event: (self.ancho_texto(event), self.ancho_texto2(event)))
        # en este punto ya tenemos un contenedor reponsivo
calculadora = App()
calculadora.mainloop()
