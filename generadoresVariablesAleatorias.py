import math
import random

class Uniforme:

    def __init__(self, a, b):
        if a>=b  :
            raise ValueError("El parametro 'A' no debe ser igual a o mayor 'B'")
            
        self.a = a
        self.b = b

    def generarNumero(self):
        return self.a + ((random.random())*(self.b-self.a))
    
class ExponencialNegativa:

    def __init__(self, lambdaArg):
        if not lambdaArg>0:
            raise ValueError("El parametro 'Lambda' debe ser mayor a 0")
        
        self.lambdaArg = lambdaArg

    def generarNumero(self):
        return -(1/self.lambdaArg)*(math.log(1-(random.random())))

class Normal:

    def __init__(self, media, dispersion):
        if not dispersion > 0:
            raise ValueError("El parametro 'Dispersión' debe ser mayor a 0")

        self.media = media
        self.dispersion = dispersion
        self.formula = 0


    def generarNumero(self):
        random1 = random.random()
        random2 = random.random()

        if (random1) == 0:
            (random1) += 1e-8

        if (random2) == 0:
            (random2) += 1e-8
        
        elif self.formula == 0:
            
            self.formula = 1
            return ((((-2*math.log((random1)))**(1/2))*(math.cos(2*math.pi*(random2))))*self.dispersion) + self.media
        
        elif self.formula == 1:
            
            self.formula = 0  
            return ((((-2*math.log((random1)))**(1/2))*(math.sin(2*math.pi*(random2))))*self.dispersion) + self.media

class Poisson:

    def __init__(self, lambdaArg):
        if not lambdaArg>0:
            raise ValueError("El parametro 'Lambda' debe ser mayor a 0")
        
        self.lambdaArg = lambdaArg

    def generarNumero(self):
        
        L = math.exp(-self.lambdaArg)
        k = -1
        p = 1

        while p > L:
            k += 1
            p *= random.random()
        
        return k
