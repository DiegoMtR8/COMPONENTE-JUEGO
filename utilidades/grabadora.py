#Librerias a utilizar
from cgitb import text
from chunk import Chunk
import pyaudio
import wave
import speech_recognition as sr
import os

class audio():
    #Se definen los parametros
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    duracion = 10
    archivo = "grabacion.wav"
    
    #r = sr.Recognizer()

    #Se inicia "pyaudio"
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    #Iniciamos grabación
    print("grabando...")
    frames=[]

    for i in range (0,int(RATE/CHUNK*duracion)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Grabación terminada")

    #Se detiene la grabación
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #Se crea/guarda el archivo de audio
    waveFile = wave.open(archivo,"wb")
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
        
    
   
    # asegurece que la ruta a "grabacion.wav" se encuentra en la misma carpeta que este script
    from os import path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "grabacion.wav")
    #AUDIO_FILE = path.join("C:\Users\IGNITER\Desktop\Nuevo_Componente\utilidades", "grabacion.wav")
    

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        #print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language="es-ES"))
        texto = r.recognize_google(audio,language="es-ES")
        #with open ("grabacion.wav","wb") as fichero:
        #    fichero.write(audio.get_wav_data())
        print("Dijiste " + r.recognize_google(audio,language="es-ES"))
    except sr.UnknownValueError:
        #print("Google Speech Recognition could not understand audio")
        print("Audio ininteligible")
    except sr.RequestError as e:
        #print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("No se pueden establece conexión con el servicio de Google Speech Recognition; {0}".format(e))

    #file = open("C:/Users/IGNITER/Desktop/Nuevo_Componente/texto.txt","w")
    file = open("C:/Users/IGNITER/Desktop/Nuevo_Componente/utilidades/texto.txt","w")
    file.write(texto)
    file.close
        
    #numero_de_letras = 0
    #with open("texto.txt","r") as file:
    #    data = file.read()
    #    lines = data.split()
    #    numero_de_letras +=len(lines)
    #    print(numero_de_letras)
    conteo = open("C:/Users/IGNITER/Desktop/Nuevo_Componente/utilidades/texto.txt","rt")
    datos = conteo.read()
    palabras = datos.split()

    print('Número de palabras en el archivo', len(palabras))
    
    