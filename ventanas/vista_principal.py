from cProfile import label
import tkinter as tk
from tkinter.font import BOLD
import utilidades.generic as utl

from ventanas.vista_prueba import vista_prueba

class vista_principal:

    def actividad_1(self):
        self.ventana.destroy()
        vista_prueba()
        
    def actividad_2(self):
        self.ventana.destroy()
        

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Objeto de Aprendizaje Oral")
        self.ventana.iconbitmap('./img/tec.ico')
        #w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry('800x500')
        self.ventana.config(bg='white')
        self.ventana.resizable(width=0,height=0)

        tec = utl.leer_imagen("./img/tec.png",(200, 200))

        #Dibujamos el frame sobre la ventana
        frame_pantalla = tk.Frame(self.ventana,bd=0,width=800,height=500,relief = tk.SOLID, padx=10, pady=10, bg='#3a7ff6')#bg='#f0f0f0')
        #Le decimos al programa en donde posicionara lo que creamos en la linea anterior
        #Side es de que lado lo queremos, fill es para mostrar en ambas direcciones y expand es para que ocupe la ventana completa
        frame_pantalla.pack(side='left',fill=tk.BOTH,expand=tk.YES)

        #Imagen
        #Posicionamos la imagen dentro del frame_pantalla que creamos y dibujamos la imagen igual le asignamos un fondo
        label = tk.Label(frame_pantalla,image=tec,bg='#600c0c')
        #Posicionamos la imagen en la esquina superior izquierda
        label.place(x=0,y=0)#(x=(280),y=0)

        #Explicación
        label2 = tk.Label(frame_pantalla,text="Objeto de Aprendizaje Oral",font=('Times',30),fg="#666a88", bg='#fcfcfc',pady=10)
        label2.place(x=250,y=0)
        #label2.pack(side='top', fill=tk.X)

        Activ_1 = tk.Button(frame_pantalla,text="Actividad 1",font=("Times",15,BOLD),bg='#3a7ff6', fg="#fff",command=self.actividad_1)
        #Activ_1.pack(side='left',fill=tk.X,expand=tk.YES)
        Activ_1.place(x=0,y=300)
        Activ_2 = tk.Button(frame_pantalla,text="Actividad 2",font=("Times",15,BOLD),bg='#3a7ff6', fg="#fff",command=self.actividad_2)
        #Activ_2.pack(side='right',fill=tk.X,expand=tk.YES)
        Activ_2.place(x=0,y=400)


        self.ventana.mainloop()