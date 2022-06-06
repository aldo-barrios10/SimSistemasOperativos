import buffer as bf
import memoria as mem
import numpy as np
import interrupciones as interr
import cache as ch

#Este archivo contiene la asignacion del sistema de archivos y de comunicacion de procesos

global contadorCache
contadorCache=0

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

#Busca subarboles para encontrar elementos
def buscarSubarbol(arbol, elemento):
    if arbol.elemento[0] == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None   

#Agrega elementos al arbol
def agregarElemento(arbol, elemento, elementoPadre, contadorCache):
    subarbol = buscarSubarbol(arbol, elementoPadre[0])
    if subarbol==None:
        buffer.eliminar()
        return print("Ruta no valida")
    existe = False
    for hijo in subarbol.hijos:
        if hijo.elemento[0] == elemento[0]:
            existe=True
    if existe == True:
        buffer.eliminar()
        
        print("Ya existe este elemento")
    else:
        subarbol.hijos.append(Arbol(elemento))
        buffer.eliminar()
        memoria.llenarmemoria(elemento[0], 20, AP)
        elementoCache=ch.ejecutar(Arbol(elemento),contadorCache,1,cache)
        print("Elemento en la cache: ", elementoCache)
        contadorCache+=1
        print("Se creó con exito")
        
#Agrega subarboles al arbol
def agregarElementoArbol(arbol, elemento, contadorCache):
    existe = False
    for hijo in arbol.hijos:
        if hijo.elemento[0] == elemento.elemento[0]:
            existe=True
    if existe == True:
        print("Ya existe este elemento")
    else:
        arbol.hijos.append(elemento)
        memoria.llenarmemoria(elemento.elemento[0], 20,AP)
        elementoCache=ch.ejecutar(elemento,contadorCache,1,cache)
        print("Elemento en la cache: ", elementoCache)
        contadorCache+=1
        print("Se creó con exito")

#Imprime elementos
def imprimirElemento(element):
    print (element[0])

#Imprime todo el arbol
def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)

#Lee el contenido de un archivo txt
def leerArchivo(arbol, elemento, contadorCache):
    if arbol==None:
        buffer.eliminar()
        return(print("No se encontó el elemento a leer"))

    for hijo in arbol.hijos:
        if elemento[0] == hijo.elemento[0]:
            if hijo.elemento[1]== 0:
                buffer.eliminar()
                memoria.leer(hijo.elemento[0],AP)
                elementoCache=ch.ejecutar(hijo,contadorCache,1,cache)
                print("Elemento en la cache: ", elementoCache)
                contadorCache+=1
                return print("Archivo vacío")
            else:
                buffer.eliminar()
                memoria.leer(hijo.elemento[0],AP)
                elementoCache=ch.ejecutar(hijo,contadorCache,1,cache)
                print("Elemento en la cache: ", elementoCache)
                contadorCache+=1
                return print(hijo.elemento[1])

#Imprime el nombre del folder y sus hijos
def imprimirFolder(arbol,elemento, contadorCache):
    subarbol = buscarSubarbol(arbol, elemento[0])
    if subarbol==None:
        buffer.eliminar()  
        return print("No se encontó el elemento")
    memoria.leer(subarbol.elemento[0],AP)
    elementoCache=ch.ejecutar(subarbol,contadorCache,1,cache)
    print("Elemento en la cache: ", elementoCache)
    contadorCache+=1
    print()
    print("Nombre de carpeta: ",subarbol.elemento[0])
    print()
    print("Contenido: ")
    
    for hijo in subarbol.hijos:
        print(hijo.elemento[0])
    print()
    buffer.eliminar()
    print()

#Elimina elementos del arbol

def eliminarTodos(arbol,elemento):
    for hijo in arbol.hijos:
        if elemento[0] == hijo.elemento[0]:
            arbol.hijos.remove(hijo)
    memoria.borrar(hijo.elemento[0], AP)        
    print("Se eliminó correctamente")
    buffer.eliminar()

#Evalua la cadena de comandos que se escribe 
def evaluarComando(cadena):
    palabra=""
    rutas=[]
    comando=[]

    for letra in cadena:
        if letra == "/":
            rutas.append(palabra)
            palabra=""
        elif letra == ":":
            comando.append(palabra)
            palabra=""
        else:
            palabra=palabra+letra

    return rutas, comando

#Nos dice si un elemento es un archivo
def esArchivo(elemento):
    return elemento.endswith('.txt')

#Cambia el nombre a carpetas y archivos
def cambiarNombre(arbol, elementoPadre,elemento, nuevoNombre, contadorCache):
    subarbol = buscarSubarbol(arbol, elementoPadre[0])
    subarbol2 = buscarSubarbol(subarbol, elemento[0])
    if subarbol2==None:
        buffer.eliminar()
        
        return(print("No se encontó el elemento"))

    for hijo in subarbol.hijos:
        if subarbol2.elemento[0] == hijo.elemento[0]:
            memoria.escribir(subarbol2.elemento[0], nuevoNombre, AP)
            elementoCache=ch.ejecutar(subarbol,contadorCache,1,cache)
            subarbol2.elemento[0]=nuevoNombre
            buffer.eliminar()
            print("Elemento en la cache: ", elementoCache)
            contadorCache+=1

#Nos permite cambiar el contenido de un archivo txt
def cambiarContenido(arbol, elemento, contenido, contadorCache):
    if arbol==None:
        return(print("No se encontó el elemento a modificar"))

    for hijo in arbol.hijos:
        if elemento[0] == hijo.elemento[0]:
            memoria.leer(hijo.elemento[0],AP)
            hijo.elemento[1]=contenido
            elementoCache=ch.ejecutar(hijo,contadorCache,1,cache)
            print("Elemento en la cache: ", elementoCache)
            contadorCache+=1

#Identifica la ruta valida para ciertas operaciones
def rutaValida(rutas):
    pasa = False
    for i in range(len(rutas)-2):
        x=buscarSubarbol(arbol1, rutas[i])
        for j in x.hijos: 
            if j.elemento[0] == rutas[i+1]:
                pasa = True
                break 
            else: 
                pasa = False
    if len(rutas)==2:
        x=buscarSubarbol(arbol1, rutas[0])
        if x!= None:
            pasa=True
    return pasa,x

#Identifica la ruta valida para ciertas operaciones con folders y archivos
def rutaValidaFolder(rutas):
    pasa = False
    for i in range(len(rutas)-1):
        x=buscarSubarbol(arbol1, rutas[i])
        for j in x.hijos: 
            if j.elemento[0] == rutas[i+1]:
                pasa = True
                break 
            else: 
                pasa = False
    return pasa,x

#Identifica la ruta valida para copiar y mover archivos
def rutaValidarCopia(rutas):
    pasa = False
    for i in range(len(rutas)):
        x=buscarSubarbol(arbol1, rutas[i])
        if x.hijos != None:
            for j in x.hijos: 
                if j.elemento[0] == rutas[i]:
                    pasa = True
                    break 
                else: 
                    pasa = False
        else:
            x=x.elemento
    return pasa,x

#Se decide la operacion en base a los comandos dados          
def decidirComando(rutas,comando, contadorCache):
    comando=comando[0]
    #Craer elementos
    if comando=="create":
        try:
            buffer.agregar(1,"Sistema de Archivos",10)
            pasa,x=rutaValida(rutas)
            elemento=rutas[-1]
            elementoPadre=rutas[-2]
            a=esArchivo(elementoPadre)
            if a:
                buffer.eliminar()
                return(print("No puedes crear un elemento dentro de un archivo"))  

            elif pasa:
                elemento=[elemento,0]
                elementoPadre=[elementoPadre,0]
                agregarElemento(x, elemento, elementoPadre, contadorCache)
            else:
                buffer.eliminar()
                print("No es una ruta valida")
        except:
            buffer.eliminar()
            return("No fue posible crear el archivo")
    #Borrar elementos
    elif comando=="delete":
        try:
            buffer.agregar(2,"Sistema de Archivos",10)
            pasa,x=rutaValidaFolder(rutas)
            elemento=rutas[-1]
            elementoPadre=rutas[-2]
            elemento=[elemento,0]
            elementoPadre=[elementoPadre,0]
            if pasa:
                eliminarTodos(x,elemento)
            else:
                buffer.eliminar()
                print("No es una ruta valida")
        except:
            buffer.eliminar()
            return("No fue posible eliminar el elemento")
    #Leer archivos
    elif comando=="read":
        try:
            buffer.agregar(3,"Sistema de Archivos",150)
            elemento=rutas[-1]
            elementoPadre=rutas[-2]
            a=esArchivo(elemento)
            pasa,x=rutaValidaFolder(rutas)
            if a and pasa:
                elemento=[elemento,0]
                elementoPadre=[elementoPadre,0]
                leerArchivo( x,elemento, contadorCache)
            else:
                buffer.eliminar()
                return print("No se puede leer un directorio")
            
        except:
            buffer.eliminar()
            return print("No fue posible leer el elemento")
    #Mostrar carpetas
    elif comando=="show":
        try:
            buffer.agregar(4,"Sistema de Archivos",150)
            elemento=rutas[-1]
            elementoPadre=rutas[-2]
            a=esArchivo(elementoPadre)
            pasa,y=rutaValidaFolder(rutas)
            if not a and pasa:
                elemento=[elemento,0]
                elementoPadre=[elementoPadre,0]
                imprimirFolder(y,elemento, contadorCache)
            else:
                buffer.eliminar()
                return print("No se puede mostrar el archivo")
            
        except:
            buffer.eliminar()
            return("No fue posible mostrar el elemento")

    else: print("Comando no valido")




if __name__ == "__main__":
    
    X1= input("Introduce el nombre de tu raiz: ")
    raiz = [X1,0]
    contadorInterrup = 0

    arbol1 = Arbol(raiz)
    buffer=bf.inicia()
    memoria,AP=mem.iniciar()
    cache=ch.iniciar()

    ejecutar=True


    while ejecutar:

        #Imprime un resumen de los elementos de la cache para visualizar su funcionamiento
        print("-----------------------RESUMEN DE CACHE Y RAM---------------------------------")
        print(cache[0].almacenamiento)
        print(cache[1].almacenamiento)
        print(cache[2].almacenamiento)
        print(cache[3].almacenamiento)
        print(cache[4].almacenamiento)
        print()

        #Se decide si hay una interrupción con probabilidad de 50%
        seleccion=np.random.randint(1,11)
        if seleccion > 5:
            contadorInterrup= interr.principal(contadorInterrup)
        print()
        cadena=input("Escriba el comando de lo que desea hacer: ")
        print()

        #Comando para cerrar el sistema
        if cadena=="close":
            ejecutar=False

        #Comando para imprimir el arbol
        elif cadena=="print":
                ejecutarProfundidadPrimero(arbol1, imprimirElemento)
                print()
        else:
            rutas,comando=evaluarComando(cadena)

            #Se toma la posibilidad de que no exista comando
            if len(comando) == 0:
                print("Comando no existente")
            
            #Renombra elementos
            elif comando[0] == "rename":
                extra=input("Ingrese el nuevo nombre: ")
                buffer.agregar(5,"Sistema de Archivos",100)
                try:
                    
                    elemento=rutas[-1]
                    elementoPadre=rutas[-2]
                    a=esArchivo(elemento)
                    pasa,x=rutaValida(rutas)

                    if pasa:
                        if a and esArchivo(extra):
                            elemento=[elemento,0]
                            elementoPadre=[elementoPadre,0]
                            cambiarNombre( x, elementoPadre,elemento, extra, contadorCache)
                        elif not(a) and not(esArchivo(extra)):
                            elemento=[elemento,0]
                            elementoPadre=[elementoPadre,0]
                            cambiarNombre( x, elementoPadre,elemento, extra, contadorCache)
                        else:
                            print("No se introdujo un nombre valido")
                            
                            buffer.eliminar()
                    else: 
                        print("No se introdujo una ruta valida")
                        buffer.eliminar()
                       
                except:
                    print("No fue posible renombrar el archivo")
                   
                    buffer.eliminar()

            #Modifica archivos txt
            elif comando[0] == "modify":
                try:
                    buffer.agregar(7,"Sistema de Archivos",110)
                    elemento=rutas[-1]
                    elementoPadre=rutas[-2]
                    a=esArchivo(elemento)
                    pasa,x=rutaValidaFolder(rutas)
                    if a and pasa:
                        extra=input("Ingrese el contenido: ")
                        elemento=[elemento,0]
                        elementoPadre=[elementoPadre,0]
                        cambiarContenido( x,elemento, extra, contadorCache)
                    elif not pasa:
                        print("No se introdujo una ruta valida")
                        buffer.eliminar()
                       
                    else:
                        print("No se puede modificar un directorio")
                        buffer.eliminar()
                        
                except:
                    print("No fue posible modificar el elemento")
                    buffer.eliminar()
                    
            #Copia elementos
            elif comando[0] == "copy":
                try:
                    buffer.agregar(8,"Sistema de Archivos",110)                
                    pasa,y=rutaValidaFolder(rutas)
                    if pasa:
                        for i in y.hijos:
                            if i.elemento[0]==rutas[-1]:
                                elemento=i

                        nuevRuta=input("Ingresa la ruta de destino: ")
                        rutas,comandos=evaluarComando(nuevRuta)
                        
                        
                        elementoPadre=[rutas[-1],0]
                        if esArchivo(elementoPadre[0]):
                            print("No puedes copiar dentro de un archivo")
                            buffer.eliminar()
                           
                        else:
                            pasar,y=rutaValidarCopia(rutas)
                            agregarElementoArbol(y,elemento, contadorCache)
                            buffer.eliminar()
                    elif not pasa:
                        print("No se introdujo una ruta valida")
                        buffer.eliminar()
                        
                    else:
                        print("No se pudo compiar correctamente")
                        buffer.eliminar()
                       
                except:
                    print("No fue posible copiar el elemento")
                    buffer.eliminar()
                    
            #Mueve elementos
            elif comando[0] == "move":
                try:  
                                
                    buffer.agregar(9,"Sistema de Archivos",110)
                    elementoB=rutas[-1]
                    elementoPadreB=rutas[-2]
                    elementoB=[elementoB,0]
                    elementoPadreB=[elementoPadreB,0]
                    pasa,x=rutaValidaFolder(rutas)
                    if pasa:
                        for i in x.hijos:
                            if i.elemento[0]==rutas[-1]:
                                elemento=i

                        nuevRuta=input("Ingresa la ruta de destino: ")
                        rutas,comandos=evaluarComando(nuevRuta)
                        
                        
                        elementoPadre=[rutas[-1],0]
                        if esArchivo(elementoPadre[0]):
                            buffer.eliminar()
                            print("No puedes copiar dentro de un archivo")
                        else:
                            pasar,y=rutaValidarCopia(rutas)
                            agregarElementoArbol(y,elemento, contadorCache)
                            eliminarTodos(x,elementoB)
                    elif not pasa:
                        buffer.eliminar()
                        print("No se introdujo una ruta valida")
                    else:
                        buffer.eliminar()
                        print("No se pudo compiar correctamente")
                except:
                    buffer.eliminar()
                    print("No fue posible copiar el elemento")


            else:
                decidirComando(rutas,comando, contadorCache)

    print()
    print("Se cerró el sistema de archivos")

    #create:Aldo_User/Carpeta 1/Prueba.txt/
    #delete:Aldo_User/Carpeta 1/Prueba.txt/
    #rename:Aldo_User/Carpeta 1/Prueba.txt/
    #show:Aldo_User/Carpeta 1/
    #modify:Aldo_User/Carpeta 1/intento.txt/
    #read:Aldo_User/Carpeta 1/intento.txt/
    #copy:
    #move:
    #print para imprimir todo
    #close para terminar programa
    