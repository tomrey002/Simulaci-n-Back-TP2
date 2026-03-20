import numpy as np

numeros = [0.2, 1.2234, 5.356, 6.4321,9.456,7.435,2.456]
numeros = np.random.uniform(0, 10, 20)

print(numeros)

max = np.max(numeros)
min = np.min(numeros)

rango = max - min
cant_numeros = numeros.size
n_bins = 2
k_numeros_intervalos = int(np.sqrt(cant_numeros))
print(k_numeros_intervalos)
frecuencias, bins = np.histogram(numeros, bins=n_bins)


print(max)
print(min)
print(rango)
print(frecuencias)
print(bins)

#  [
#  { "binStart": 0, "binEnd": 10, "freq": 12 },
#  { "binStart": 10, "binEnd": 20, "freq": 50 },
#  { "binStart": 20, "binEnd": 30, "freq": 18 },
#  { "binStart": 30, "binEnd": 40, "freq": 7 }
# ]
bins = bins.tolist()
frecuencias = frecuencias.tolist()

contenedores = []

for i in range(len(bins)-1):
    datos = {"binStart": bins[i], "binEnd": bins[i+1], "freq": frecuencias[i] }
    contenedores.append(datos)
    print(i)

print(contenedores)