from cProfile import label
from tkinter import W, ttk, StringVar, Text
from tkinter.font import BOLD
import tkinter as tk
from utilidades.record import record
import random as r

class vista_prueba:

    def calif(self):
        dato = revis
        numero_palabra=0
        retro = ""
        txt = open('texto.txt','r',encoding="utf-8")
        mensaje = txt.read()
        por_palabra = str(mensaje).split()
        for palabra in por_palabra:
            if palabra[0].upper() == dato:
                print(palabra)
                numero_palabra += 1
                #print(numero_palabra)
                calificacion = numero_palabra
                if calificacion <= 3:
                    retro = "Hola Mundo 1"
                    retroa = StringVar()
                    retroa.set(retro)
                    LabelPal = tk.Label(self.frame_activ_1, textvariable=retroa, relief='raised',font=("Times",15,BOLD))
                    LabelPal.place(x=200,y=200)
                    #print(retro)
                else:
                    if calificacion > 3 and calificacion <=5:
                        retro = "Hola Mundo 2"
                        retroa = StringVar()
                        retroa.set(retro)
                        LabelPal = tk.Label(self.frame_activ_1, textvariable=retroa, relief='raised',font=("Times",15,BOLD))
                        LabelPal.place(x=200,y=200)
                        #print(retro)
                    else:
                        if calificacion > 5 :
                            retro = "Hola mundo 3"
                            retroa = StringVar()
                            retroa.set(retro)
                            LabelPal = tk.Label(self.frame_activ_1, textvariable=retroa, relief='raised',font=("Times",15,BOLD))
                            LabelPal.place(x=200,y=200)
                            #print(retro)
                            return retro
                #return retro
        #return retro
        print(retro)
        txt.close()

        #print(calificacion)
        
        #print(dato)
        #txt.close()
    

    def biblio(self):
        diccionario={'1':'S', '2':'R', '3':'N', '4':'D', '5':'L', '6':'A'}
        var = r.choice(list(diccionario.values()))
        print(var)
        return var

    def grabar(self):
        record()
        self.calif()
        #self.ventana.destroy()

    def __init__(self):

        self.ventana=tk.Tk()
        self.ventana.title("Actividad 1")
        self.ventana.iconbitmap('./img/tec.ico')
        self.ventana.geometry('800x500')
        self.ventana.resizable(width=0,height=0)

        
        global revis
        revis=self.biblio()
        inst = StringVar()
        inst.set(f"Menciona tantas palabras con la letra {revis} como puedas")

        #Palab=self.calif()
        #Pal=StringVar()
        #Pal.set(f"Retroalimentación {Palab}")


        self.frame_activ_1 = tk.Frame(self.ventana,bd=0,width=800,height=500,relief = tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        self.frame_activ_1.pack(side='left',fill=tk.BOTH,expand=tk.YES)

        LabelInst = tk.Label(self.frame_activ_1, textvariable=inst, relief='raised',font=("Times",15,BOLD))
        LabelInst.place(x=100,y=100)
        
        inicio = tk.Button(self.frame_activ_1,text='Iniciar Grabación',font=("Times",15,BOLD),bg='#3a7ff6', fg="#fff",command=self.grabar)
        inicio.place(x=400,y=400)
        inicio.config()

        #LabelPal = tk.Label(self.frame_activ_1, textvariable=Palab, relief='raised',font=("Times",15,BOLD))
        #LabelPal.place(x=200,y=200)
        
        #vista_texto = tk.Label(frame_activ_1)
        #vista_texto.place(x=400,y=400)

        self.ventana.mainloop()