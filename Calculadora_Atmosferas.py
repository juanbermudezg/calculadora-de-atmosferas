from PIL import Image
from PIL import ImageTk
from tkinter.ttk import *
import webview
import tkinter
from tkinter import filedialog
import tkinter.font as tkFont
import webbrowser
from tkinter import ttk
euler=2.71828
frontera_Internacional=11000
constante_Internacional=287
gravedad_Internacional=9.81
temperatura_Inicial_Internacional=288.15
temperatura_11_Internacional=216.65
presion_11_Internacional=22385.19791
gradiente_Tropofera=-0.0065
gradiente_Estratosfera=0
densidad_Incial_Internacional=1.225
densidad_Incial_Imperial=0.002355
presion_Inicial_Internacional=101325
presion_Incial_Imperial=2215.22
temperatura_Temp=0
densidad_Temp=0
presion_Temp=0
Gringo=1#1 es imperial, 0 es internacional
class window1():
    def __init__(self):
            #custom_font = tkFont.Font(family="Lumos", size=60, weight="bold")
            self.vari=False
            self.ventana = tkinter.Tk()
            
            self.ventana.geometry("1920x1080")
            self.ventana.configure(bg="white")
            self.ventana.resizable(width=False, height=False)
            self.ventana.title("Calculadora de atmósferas - Inicio")
            self.var=""
            
            self.etiqueta = tkinter.Label(self.ventana, text = "Calculadora de atmósferas", bg = "gray99", font=("Times ", 60, "bold"))
            self.etiqueta.pack(fill=tkinter.X)
            self.etiquet3 = tkinter.Label(self.ventana, text = "", bg="white", font="Times 10")
            self.etiquet3.pack(fill=tkinter.X)
           
            self.esave=tkinter.PhotoImage(file='esave.png')
            photoimage_esave = self.esave.subsample(25) 
  
            self.esave_b=tkinter.Button(self.ventana, text = 'Escuela de Aviación del Ejército - ESAVE',font="Times 15",bg="white", command= self.esavep, image = photoimage_esave, 
                    compound = "left").pack(side = "top")
            
            self.etiqueta6=tkinter.Label(self.ventana, text="", bg="white", font="Times 30")
            self.etiqueta6.pack()
            
            
            self.etiqueta5=tkinter.Label(self.ventana, text="Creado por Juan Andrés Bermúdez Gómez", bg="white", font="Times 30")
            self.etiqueta5.pack()
            self.linkedln=tkinter.PhotoImage(file='linkedln.png')
            photoimage_linkedln = self.linkedln.subsample(10) 
  
            self.linkedln_b=tkinter.Button(self.ventana, command= self.linkedinp, image = photoimage_linkedln, 
                    compound = "top", bg="white")
            self.linkedln_b.config(width=100, height=100)
            self.linkedln_b.pack()

            self.github=tkinter.PhotoImage(file='github.png')
            photoimage_github = self.github.subsample(10) 
            self.etiqueta8=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta8.pack()
            self.github_b=tkinter.Button(self.ventana, command= self.githubp, image = photoimage_github, 
                    compound = "top", bg="white")
            self.github_b.config(width=100, height=100)
            self.github_b.pack()
            
            
            self.etiqueta6=tkinter.Label(self.ventana, text="", bg="white", font="Times 30")
            self.etiqueta6.pack()

            
            self.botonSalida = tkinter.Button(self.ventana, text="Empezar a calcular", padx=50, pady=10, font="Times 15", bg="gray99", fg="black", command= lambda: [self.ventana2()])
            self.botonSalida.pack()
            self.etiqueta16=tkinter.Label(self.ventana, text="", bg="white", font="Times 30")
            self.etiqueta16.pack()
            self.botonSalida = tkinter.Button(self.ventana, text="Exit", padx=50, pady=10, font="Times 15", bg="black", fg="white", command= lambda: [self.ventana.destroy()])
            self.botonSalida.pack()
            self.ventana.mainloop()
    def selectionFolder(self):
                self.folder=filedialog.askdirectory(title="Folder", initialdir="C:/")
    def esavep(self):
            webview.create_window('Escuela de Aviación del Ejército', 'https://www.esave.mil.co')
            webview.start()
    def linkedinp(self):
            webbrowser.open('https://www.linkedin.com/in/juanbermudezgomez/')
            webview.create_window('Linkedin - Desarrollador', 'https://www.linkedin.com/in/juanbermudezgomez/')
            webview.start()
    def githubp(self):
            webbrowser.open('https://github.com/juanbermudezg')
            webview.create_window('GitHub - Desarrollador', 'https://github.com/juanbermudezg')
            webview.start()
    def ventana2(self):
        self.ventana.destroy() 
        window2()

class window2():
    
    def __init__(self):
            
            self.vari=False
            self.ventana = tkinter.Tk()
            self.ventana.geometry("1920x1080")
            self.ventana.configure(bg="white")
            self.ventana.resizable(width=False, height=False)
            self.ventana.title("Calculadora de atmósferas - Magnitudes")
            self.var=""
            self.etiqueta = tkinter.Label(self.ventana, text = "Escribe el valor de la altura", bg = "gray99", font=("Times ", 30, "bold"))
            self.etiqueta.pack(fill=tkinter.X)
            self.etiqueta17=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta17.pack()
            self.magnitude = tkinter.Entry(self.ventana, font="Times 15", bg = "snow")
            self.magnitude.pack()
            self.etiqueta18=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta18.pack()
            self.etiqueta1 = tkinter.Label(self.ventana, text = "¿Cuál es la unidad de medida?", bg = "gray99", font=("Times ", 15))
            self.etiqueta1.pack(fill=tkinter.X)
            self.etiqueta15=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta15.pack()
            
            self.style2 = Style(self.ventana) 
            self.style2.configure("TRadiobutton", background = "white",  
                foreground = "black", font = ("Times", 15))
            self.clase10   = tkinter.IntVar()
            self.clase11 = ttk.Radiobutton(self.ventana, text='Metros (m)', 
                                      variable=self.clase10, value=1)
            self.clase11.pack()
            self.clase22 = ttk.Radiobutton(self.ventana, text='Kilometros (km)', 
                                      variable=self.clase10, value=2)
            self.clase22.pack()
            self.clase33 = ttk.Radiobutton(self.ventana, text='Pies (ft)', 
                                      variable=self.clase10, value=3)
            self.clase33.pack()
            self.clase44 = ttk.Radiobutton(self.ventana, text='Pulgadas (in)', 
                                      variable=self.clase10, value=4)
            self.clase44.pack()
            self.etiqueta16=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta16.pack()
            self.etiqueta4=tkinter.Label(self.ventana, text="¿Los resultados deben mostrarse en cuál sistema?", bg="white", font="Times 15")
            self.etiqueta4.pack()
            self.style = Style(self.ventana) 
            self.style.configure("TRadiobutton", background = "white",  
                foreground = "black", font = ("Times", 15))
            self.clase   = tkinter.IntVar()
            self.clase1 = ttk.Radiobutton(self.ventana, text='Imperial', 
                                      variable=self.clase, value=1)
            self.clase1.pack()
            
            self.clase2 = ttk.Radiobutton(self.ventana, text='Internacional', 
                                      variable=self.clase, value=2)
            self.clase2.pack()

            self.etiqueta19=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta19.pack()

            self.botonAcceso = tkinter.Button(self.ventana, text="¡Calcular!", padx=100, pady=20, font="Times 20", bg = "white", command= self.verificationData)
            self.botonAcceso.pack()
            self.etiqueta20=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta20.pack()

            self.botonSalida = tkinter.Button(self.ventana, text="Salir", padx=50, pady=10, font="Times 15", bg="black", fg="white", command= lambda: [self.ventana.destroy()])
            self.botonSalida.pack()

    def verificationData(self):
        
        try:
            
            self.magnitud1=float(self.magnitude.get())          
        except:
            self.magnitude.delete(0,tkinter.END)
            self.mensaje="Verifica que en la magnitud escribiste un número o llenaste los datos correctamente"
            tkinter.messagebox.showinfo("Error", self.mensaje)
        self.hacerOperacion()
 
    def hacerOperacion(self):
                global temperatura_Temp
                global densidad_Temp
                global presion_Temp
                global Gringo
                
                if self.clase10.get() == 1:
                    if self.magnitud1 <=frontera_Internacional:
                        temperatura_Temp=temperatura_Inicial_Internacional+(gradiente_Tropofera*self.magnitud1)
                        presion_Temp=presion_Inicial_Internacional*(temperatura_Temp/temperatura_Inicial_Internacional)**(-(gravedad_Internacional/(constante_Internacional*gradiente_Tropofera)))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                       
                    else:
                        temperatura_Temp=temperatura_11_Internacional
                        presion_Temp=presion_11_Internacional*euler**(-gravedad_Internacional/(constante_Internacional*temperatura_Temp)*(self.magnitud1-frontera_Internacional))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                elif self.clase10.get()==2:
                    self.magnitud1=self.magnitud1*1000
                    if self.magnitud1 <=frontera_Internacional:
                        temperatura_Temp=temperatura_Inicial_Internacional+(gradiente_Tropofera*self.magnitud1)
                        presion_Temp=presion_Inicial_Internacional*(temperatura_Temp/temperatura_Inicial_Internacional)**(-(gravedad_Internacional/(constante_Internacional*gradiente_Tropofera)))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                    else:
                        temperatura_Temp=temperatura_11_Internacional
                        presion_Temp=presion_11_Internacional*euler**(-gravedad_Internacional/(constante_Internacional*temperatura_Temp)*(self.magnitud1-frontera_Internacional))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                elif self.clase10.get()==3:
                    self.magnitud1=self.magnitud1/3.281
                    if self.magnitud1 <=frontera_Internacional:
                        temperatura_Temp=temperatura_Inicial_Internacional+(gradiente_Tropofera*self.magnitud1)
                        presion_Temp=presion_Inicial_Internacional*(temperatura_Temp/temperatura_Inicial_Internacional)**(-(gravedad_Internacional/(constante_Internacional*gradiente_Tropofera)))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                        
                    else:
                        temperatura_Temp=temperatura_11_Internacional
                        presion_Temp=presion_11_Internacional*euler**(-gravedad_Internacional/(constante_Internacional*temperatura_Temp)*(self.magnitud1-frontera_Internacional))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                elif self.clase10.get()==4:
                    self.magnitud1=self.magnitud1/39.37
                    
                    if self.magnitud1 <=frontera_Internacional:
                        temperatura_Temp=temperatura_Inicial_Internacional+(gradiente_Tropofera*self.magnitud1)
                        presion_Temp=presion_Inicial_Internacional*(temperatura_Temp/temperatura_Inicial_Internacional)**(-(gravedad_Internacional/(constante_Internacional*gradiente_Tropofera)))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                        
                    else:
                        temperatura_Temp=temperatura_11_Internacional
                        presion_Temp=presion_11_Internacional*euler**(-gravedad_Internacional/(constante_Internacional*temperatura_Temp)*(self.magnitud1-frontera_Internacional))
                        densidad_Temp=presion_Temp/(temperatura_Temp*constante_Internacional)
                        
                self.a=self.clase.get()
                if self.a == 1:
                    temperatura_Temp=(temperatura_Temp-273.15)*9/5+32
                    presion_Temp=presion_Temp/(6895*144)
                    densidad_Temp=densidad_Temp/515.4
                    Gringo=1
                    print(temperatura_Temp)
                else:
                    Gringo=0
                self.ventana.destroy()
                window3()
                
class window3():
    def __init__(self):
            self.vari=False
            self.ventana = tkinter.Tk()
            self.ventana.geometry("1920x1080")
            self.ventana.configure(bg="white")
            self.ventana.resizable(width=False, height=False)
            self.ventana.title("Calculadora de atmósferas - Resultados")
            self.var=""
            self.etiqueta1=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta1.pack()
            self.etiqueta = tkinter.Label(self.ventana, text = "Resultados", bg = "gray99", font=("Times ", 30, "bold"))
            self.etiqueta.pack(fill=tkinter.X)
            self.etiqueta17=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta17.pack()
            if Gringo==1:
                self.resultado_Temperatura=str(temperatura_Temp)+" °F"
                self.resultado_Presion=str(presion_Temp)+" lb/ft^2"
                self.resultado_Densidad=str(densidad_Temp)+" slug/ft^3"
            else:
                self.resultado_Temperatura=str(temperatura_Temp)+" K"
                self.resultado_Presion=str(presion_Temp)+" Pa"
                self.resultado_Densidad=str(densidad_Temp)+" kg/m^3"
            self.etiqueta3=tkinter.Label(self.ventana, text="Temperatura:", bg="white", font=("Times ", 20, "bold"))
            self.etiqueta3.pack()
            self.etiqueta2=tkinter.Label(self.ventana, text=self.resultado_Temperatura, bg="white", font="Times 15")
            self.etiqueta2.pack()
            self.etiqueta4=tkinter.Label(self.ventana, text="Presión:", bg="white", font=("Times ", 20, "bold"))
            self.etiqueta4.pack()
            self.etiqueta5=tkinter.Label(self.ventana, text=self.resultado_Presion, bg="white", font="Times 15")
            self.etiqueta5.pack()
            self.etiqueta6=tkinter.Label(self.ventana, text="Densidad:", bg="white", font=("Times ", 20, "bold"))
            self.etiqueta6.pack()
            self.etiqueta7=tkinter.Label(self.ventana, text=self.resultado_Densidad, bg="white", font="Times 15")
            self.etiqueta7.pack()
            self.etiqueta17=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta17.pack()
            self.botonAtras = tkinter.Button(self.ventana, text="Volver", padx=50, pady=10, font="Times 15", bg="snow", fg="black", command= lambda: [window2(),self.ventana.destroy()])
            self.botonAtras.pack()
            self.etiqueta20=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta20.pack()
            self.botonPaso = tkinter.Button(self.ventana, text="Paso a paso", padx=50, pady=10, font="Times 15", bg="snow", fg="black", command= lambda: [self.paso()])
            self.botonPaso.pack()
            self.etiqueta22=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta22.pack()
            self.imagen = Image.open("img1.png")
            self.imagen_tk = ImageTk.PhotoImage(self.imagen)
            self.etiqueta23=tkinter.Label(self.ventana, image=self.imagen_tk)
            self.etiqueta23.pack()
            self.etiqueta29=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta29.pack()
            self.botonSalida = tkinter.Button(self.ventana, text="Salir", padx=50, pady=10, font="Times 15", bg="black", fg="white", command= lambda: [self.ventana.destroy()])
            self.botonSalida.pack()
            self.etiqueta18=tkinter.Label(self.ventana, text="", bg="white", font="Times 15")
            self.etiqueta18.pack()
            

    def paso(self):
        self.mensaje="Funcionalidad implementada proximamente"
        tkinter.messagebox.showinfo("Pardon moi", self.mensaje)

def main():
    window1()
main()