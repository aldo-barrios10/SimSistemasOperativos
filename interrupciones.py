
import numpy as np


#Este archivo contiene la asignación de interrupciones 

#Interrupcion que nos a da un contador de interrupciones, es auxiliar de la funcion interrupcion3
def intreset():
    try:
        print("---------------------------Interrupción 3----------------------------")
        print("1- Continuar",'\n')
        print("2- Reiniciar",'\n')
        z= int(input("¿Qué deseas hacer? (Ingresa el número): "))
        print()
        return z
    except:
        print("No se ingresó un numero")
        return 0

#Interrupcion 1 que nos pide numeros y los suma
def interrupcion1(contador):
    try:
        print()
        print("---------------------------Interrupcion 1----------------------------")
        x= int(input("Ingresa el primer número: ")) 
        y=int(input("Ingresa el segundo número: ")) 
        resultado = x+y
        print(resultado)
        print('\n')
        contador +=1
        return contador
    except:
        print("No se ingreso un numero para sumar")
        return contador

#Interrupcion 2 que nos pide ingresar cualquier caracter
def interrupcion2(contador):
    print()
    print("---------------------------Interrupcion 2-----------------------------") 
    x= input("Ingresa cualquier caracter para continuar: ")
    print("Se seleccionó: ", x)
    print('\n')
    contador +=1
    return contador 

#Interrupcion 3 que nos permite reiniciar el contador o reiniciarlo
def interrupcion3(contador):
    y = intreset()
    if y == 1:
        contador +=1
        return contador
    elif y == 2:
        contador = 0
        return contador
    else:
        print("Seleccion no valida para interrupcion, el proceso continuará")
        return contador


#Se selecciona una interrupcion al azar 
def principal(contador):
    seleccion=np.random.randint(1,4)
    if seleccion == 1:
        con=interrupcion1(contador)

    elif seleccion == 2:
        con=interrupcion2(contador)
        
    elif seleccion == 3:
        con=interrupcion3(contador)
    
    print("Contador de interrupciones: ", con)

    return con
    
            

