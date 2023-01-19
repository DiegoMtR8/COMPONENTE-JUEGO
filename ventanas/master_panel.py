import tkinter as tk
from tkinter.font import BOLD
import utilidades.generic as utl
from ventanas.vista_principal import vista_principal
#from utilidades.dict import dict

class MasterPanel:

    def verificar(self):
        self.ventana.destroy()
        vista_principal()

    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title("Bienvenida")
        self.ventana.iconbitmap('./img/tec.ico')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana,800,500)
        #self.diccionario()
        #self.muestra=dict().biblio()

        logo = utl.leer_imagen("./img/tec.png",(200, 200))

        #frame logo lado izquiero
        #Esta linea maneja el borde del lado izquiero del frame (La linea bajo este aviso)
        frame_logo = tk.Frame(self.ventana,bd=0,width=300,relief = tk.SOLID, padx=10, pady=10,bg='#600c0c') #bg='#3a7ff6')#borde azul cielo
        #Esta linea ubica en donde se encontrara lo que hemos creado (la parte del frame que contiene la imagen)
        frame_logo.pack(side="left",expand=tk.NO, fill=tk.BOTH)
        #Esta linea maneja el relleno del lado izquiero del frame e inserta la imagen
        label = tk.Label(frame_logo,image=logo,bg='#600c0c')#bg='#3a7ff6')#fondo
        #Esta linea posiciona el label en el mero centro de la parte izquiera del frame (Porque esta divido en 2)
        label.place(x=0,y=0,relwidth=1,relheight=1)

        #frame form lado derecho
        #Esta linea maneja el lado derecho del frame (en donde esta la bienvenida)
        frame_form = tk.Frame(self.ventana,bd=0,width=500,relief = tk.SOLID, bg='white')#bg='#fcfcfc')
        #Esta linea maneja de que lado se encontrara el formulario (en este caso el lado derecho)
        frame_form.pack(side="right",expand=tk.YES, fill=tk.BOTH)

        #frame_form_top
        #Esta linea inserta dentro de nuestro frame_form (lado derecho) 
        frame_form_titulo = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='white')
        frame_form_titulo.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_titulo,text="Objeto de Aprendizaje Oral",font=('Times',30),fg="#666a88", bg='#fcfcfc',pady=10)
        title.pack(expand=tk.YES,fill=tk.BOTH, pady=(100,0))


        frame_form_subtit = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='blue')
        frame_form_subtit.pack(side="top",fill=tk.X)
        title2 = tk.Label(frame_form_subtit,text="Bienvenido",font=('Times',20),fg="#666a88", bg='#fcfcfc')
        title2.pack(expand=tk.YES,fill=tk.BOTH)

        #frame_form_saludo
        frame_form_fill= tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="top",expand=tk.YES,fill=tk.BOTH)

        inicio = tk.Button(frame_form_fill,text="Iniciar",font=("Times",15,BOLD),bg='#3a7ff6', fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        #inicio.bind("return",lambda event: self.verificar())

        self.ventana.mainloop()