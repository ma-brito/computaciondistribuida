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


def main():
    # El primer argumento es el nombre de la función
    function_name = sys.argv[1]
    # El segundo argumento es la dimensión del problema
    d = int(sys.argv[2])
    # Los argumentos restantes son los valores de x_i
    xx = [float(arg) for arg in sys.argv[3:]]

    if len(xx) != d:
        print(f"Error: Se esperaban {d} valores para xx, pero se recibieron {len(xx)}")
        return

    if function_name == "schwefel":
        result = schwefel(xx)
    elif function_name == "rotated_hyper_ellipsoid":
        result = rotated_hyper_ellipsoid(xx)
    else:
        print(f"Error: Función desconocida '{function_name}'")
        return

    print("El valor de la función es:", result)

if __name__ == "__main__":
    main()
