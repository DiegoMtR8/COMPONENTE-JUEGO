from chunk import Chunk
from ssl import CHANNEL_BINDING_TYPES
import pyaudio
import wave
from os import path
import speech_recognition as sr
#from ventanas.vista_revision import vista_revision
from utilidades.calificar import calificacion


class record():
    
    def conteo(self):
        numpalabras = 0
        
        with open("texto.txt","r") as fichero:
            for linea in fichero:
                palabras = linea.split()
                for palabras in palabras:
                    numpalabras += 1
        print('El texto contiene %s palabras' %numpalabras)
        #vista_revision()
        #calificacion()
        return numpalabras

    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.duracion = 10
        self.archivo = "record.wav"
    
        #Se inicia PyAudio
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)
        
        print("grabando...")
        frames=[]
        
        for i in range (0, int(self.RATE/self.CHUNK*self.duracion)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        print("Grabación terminada")
        
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        #Se crea el archivo de audio
        waveFile = wave.open(self.archivo,"wb")
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        
        #Se comienza el proceso de imprimir el audio al txt
        
        #Definimos el archivo de audio que usaremos
        grabacion = "record.wav"
        
        #Se inicia el reconocedor de voz
        re = sr.Recognizer()
        
        #Conversion de audio a texto
        with sr.AudioFile(grabacion) as source:
            #obtenemos la información del audio
            info_audio = re.record(source)
            #Conversión a texto
            texto = re.recognize_google(info_audio, language="es-ES")
            #Se imprime el texto
            print(texto)
            
        #Crear el archivo de texto y guardar el audio en el
        file = open("texto.txt","w",encoding="utf-8")

        cant = 0
        palabra2 = str(texto).split()
        print(palabra2)
        for palabra in palabra2:
            if cant <= 3:
                file.write(palabra+" ")
                cant+=1
            elif(cant >3):
                cant= 0
                file.write(palabra+"\n")
        
        file.close()
        self.conteo()
        #vista_revision()
        #num = self.conteo()
        #print(num)