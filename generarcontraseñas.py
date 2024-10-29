#creamos contraseñas con longitud

#importamos librerias

import string
import random

#creamos una variable que pida una longitud a un usuario

long = int(input("Ingrese la longitud de la contraseña"))
        #con el input hacemos que el usuario pueda introducir datos

caracteres = string.ascii_letters + string.digits + string.punctuation
            #ascii_letters -> permite introducir mayusculas o minusculas
            #digits -> " " números del 1-9
            #punctiation -> " " signos de puntuación

contraseña = "".join(random.choice(caracteres) for i in range(long));
    
    #joim se usa para unir elemntos, en este caso,
    #  lo que introduzca el usuario por la interfaz
    #usamos la libreria random que con .choice elegira datos introducidos
    #usamos un for (i es la posicion) para limitar la long


print("la contraseña generada es: " + contraseña)
