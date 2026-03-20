import generadoresVariablesAleatorias as gva
import numpy as np

class GeneradorNumeros:

    def __init__(self, objetoRequest, decimales=4):
        # if ("Uniforme", "ExponencialNegativa", "Normal" ) not in objetoRequest["distribucion"]:
        #     raise ValueError("Ingresar una distribución conocida para el programa")
        
        self.cantidadNumeros = int(objetoRequest["cantidadNumeros"])
        self.distribucionNombre = objetoRequest["distribucion"]
        self.decimales = decimales

        match self.distribucionNombre:
            
            case "Uniforme":
                self.distribucionInstanciada = gva.Uniforme(float(objetoRequest["parametros"]["A"]), float(objetoRequest["parametros"]["B"]))

            case "ExponencialNegativa":
                self.distribucionInstanciada = gva.ExponencialNegativa(objetoRequest["parametros"]["Lambda"])
            
            case "Normal":
                self.distribucionInstanciada = gva.Normal(objetoRequest["parametros"]["Media"], objetoRequest["parametros"]["Desviacion"])
            case "Poisson":
                self.distribucionInstanciada = gva.Poisson(objetoRequest["parametros"]["Lambda"])
                self.decimales = 0
            

    def generarVectorDeNumeros(self):
        
        vectorDeNumeros = []


        for i in range(self.cantidadNumeros):
            valorGenerado = self.truncar_numero(self.distribucionInstanciada.generarNumero())
            
            vectorDeNumeros.append(valorGenerado)
    
        return vectorDeNumeros
    

    
    def truncar_numero(self, numero):
        if self.decimales == 0:
            return int(numero)

        else:
            return int(numero * (10**self.decimales)) / (10**self.decimales)


class GenerarDatosHistograma:

    def __init__(self, datos, decimales=4):
        
        self.numeros = np.array(datos["numeros"])
        
        if (datos["intervalos"] < 50):
            self.intervalos = datos["intervalos"]
        else:
            self.intervalos = 50 
        
        self.decimales = decimales
    
    def generar_datos_histograma_object(self):
        frecuencias, bins = np.histogram(self.numeros, bins=self.intervalos)
        bins = bins.tolist()
        frecuencias = frecuencias.tolist()

        contenedores = []
        
        for i in range(len(bins)-1):
            datos = {"binStart": self.truncar_numero(bins[i]), "binEnd": self.truncar_numero(bins[i+1]), "freq": frecuencias[i] }
            contenedores.append(datos)
        
        return contenedores
    
    def truncar_numero(self, numero):
        if self.decimales == 0:
            return int(numero)

        else:
            return int(numero * (10**self.decimales)) / (10**self.decimales)