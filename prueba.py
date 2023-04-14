#Importar librerías
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
#Conexion base de datos
#import sqlite3

#Data analysis
#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd

#Trabajar con apis
import requests
import json

#Trabajar con colorpicker
#from tkinter import colorchooser

#Crear Tabs
#from tkinter import ttk

def mostrar_respuesta(clima):
    
    try:
        nombre_ciudad = clima["name"]
        nombre_pais = clima["sys"]["country"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        pais["text"] = nombre_pais
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"]="intenta nuevamente"

def clima_JSON(ciudad):
    try:
        API_key = "871f93a0ef945a6f142809e5b078c5c2"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID": API_key, "q": ciudad, "units": "metric", "lang":"es"}
        response = requests.get(URL, params= parametros)
        clima = response.json()
        mostrar_respuesta(clima)
    except:
        print("Error")

    #Testing API
    #print(response.json())
    #print(clima["name"])
    #print(clima["country"])
    #print(clima["weather"][0]["description"])
    #print(clima["main"]["temp"])



    
#Crear ventana - Parametros basicos
ventana = Tk()
ventana.title("App del Clima")
ventana.iconbitmap('img/basedatos.ico')
ventana.geometry("350x550")
ventana.configure(bg="#7C96AB")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify= "center")
texto_ciudad.pack(padx=30, pady=30)

obtener_clima = Button(ventana, text= "Obtener Clima", font=("Courier",20, "normal"), command= lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font= ("Courier",20, "normal"), bg="#7C96AB")
ciudad.pack(padx=30, pady=30)

pais = Label(font= ("Courier",20, "normal"), bg="#7C96AB")
pais.pack(padx=30, pady=30)

temperatura = Label(font= ("Courier",30, "normal"), bg="#7C96AB")
temperatura.pack(padx=30, pady=30)

descripcion = Label(font= ("Courier",20, "normal"), bg ="#7C96AB")
descripcion.pack(padx=30, pady=30)



#Bucle infinito (Mantiene abierta la ventana/ aplicación)
ventana.mainloop()