import numpy as np
import sys

def rotated_hyper_ellipsoid(xx):
    d = len(xx)
    outer = 0
    for ii in range(d):
        inner = 0
        for jj in range(ii+1):
            xj = xx[jj]
            inner = inner + xj**2
        outer = outer + inner
    return outer

def schwefel(xx):
    d = len(xx)
    total = 0
    for ii in range(d):
        xi = xx[ii]
        total = total + xi * np.sin(np.sqrt(abs(xi)))
    y = 418.9829 * d - total
    return y

''' El programa deberá recibir como parámetros:
i) Función objetivo [ Esto puede pasarse como un número o una
cadena, para elegir alguna de las descritas anteriormente]
ii) Dimensión, que se utilizará para definir el espacio de búsqueda
correspondiente
iii) Número total de iteraciones a realizar
iv) Intervalo de búsqueda

El programa deberá devolver, e imprimir en pantalla, el resultado de la búsqueda
imprimiendo el valor de x ( la mejor solución encontrada), así como su evaluación.

Ejemplo de ejecución y resultado esperado:
$ busqueda_aleatoria sphere 2 1000
Función: sphere
Dimensión del problema: 2
Total de iteraciones: 1000
Mejor solución encontrada:
x = [ 0.1 1.2 ]
f(x) = 300.86 '''
def main():
    print("hola")
    funcion = sys.argv[1]
    d = int(sys.argv[2])

    iteraciones = int(sys.argv[3])
    intervalo = (float(sys.argv[4]), float(sys.argv[5]))  # Captura ambos límites del intervalo 
    result = float('inf')
    mejor_solucion = 0
    print("funcion: ", funcion)
    while iteraciones > 0:
        xx = np.random.uniform(intervalo[0], intervalo[1], size=d) 
        if funcion == "schwefel":
            if result > schwefel(xx):
                result = schwefel(xx)
                mejor_solucion = xx
        elif funcion == "rotated_hyper_ellipsoid":
            if result > rotated_hyper_ellipsoid(xx):
                result = rotated_hyper_ellipsoid(xx)
                mejor_solucion = xx
        iteraciones -= 1
    print("Función: ", funcion)
    print("Dimensión del problema: ", d)
    print("Total de iteraciones: ", iteraciones)
    print("Mejor solución encontrada:")
    print("x = ", mejor_solucion)
    print("f(x) = ", result)

if __name__ == "__main__":
    main()


        

