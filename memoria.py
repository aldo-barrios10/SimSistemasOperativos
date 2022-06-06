import numpy as np

#Este archivo contiene la reposicion de paginas y el almacenamiento en las mismas

class pagina: 

    def __init__(self,capacidad, id):
        self.id = id
        self.cappag = int(capacidad/4)
        self.almacenamiento= []
        self.contadorUso = 0 

    #Introducir elementos a una pagina
    def introducirpagina(self, elemento,peso, contPag, AP):

        AP.verificar(self)
        AP.mostrar()
        if self.cappag - peso > 0:
            self.almacenamiento.append(elemento)
        else: 
            return print("Pagina llena llena")

    #Eliminar elementos a una pagina
    def borrarPagina(self, idelemento, AP):
        AP.verificar(self)
        AP.mostrar()
        for i in self.almacenamiento:
            if idelemento == i[0]:
                self.almacenamiento.remove(i)

    #Cambiar elementos a una pagina
    def escribirPagina(self,idB, elementoNuev, AP):
        AP.verificar(self)
        AP.mostrar()
        for i in self.almacenamiento:
            if idB == i[0]:
                i[1]=elementoNuev


    def uso(self):
        self.contadorUso=0

    def noUso(self):
        self.contadorUso+=1


class primario:

    def __init__(self, tamano):
        self.tamano = tamano
        self.contenido = []

    #Repone la pagina deseada buscando al contador más alto y eliminandola
    def reponer(self, pagina):

        if len(self.contenido) == self.tamano:
            aux=0
            for elemento in self.contenido:
                aux2=elemento.contadorUso
                if aux2 > aux:
                    aux= aux2
            
            for elemento in self.contenido:
                if aux == elemento.contadorUso:
                    elemaux=elemento
                else:
                    elemento.contadorUso +=1

            elemaux.contadorUso =0
            self.contenido.remove(elemaux)
            self.contenido.append(pagina)

        else:
            for elemento in self.contenido:
                elemento.contadorUso +=1

            self.contenido.append(pagina)
    
    #Verifica si se encuentra la pagina en la principal, de no ser asi la repone
    def verificar(self, pagina):
        
        if pagina in self.contenido:
            indice=self.contenido.index(pagina)
            for elemento in self.contenido:
                elemento.contadorUso +=1
            
            self.contenido[indice].contadorUso=0
        
        else:
            self.reponer(pagina)

    def mostrar(self):
        print()
        print("---------------CONTENIDO DE REPOSICION DE PAGINAS--------------")
        print()

        for elemento in self.contenido:
            print("Pagina: ", elemento.id, ", contador de uso reciente: ", elemento.contadorUso)
        
        print()

class memoria: 

    def __init__(self,capacidad):
        self.capacidad=capacidad
        self.contadorid=0
        self.cappag = int(capacidad/4)
        self.memoria= []
        self.Pag1=pagina(3200,1)
        self.Pag2=pagina(3200,2)
        self.Pag3=pagina(3200,3)  
        self.Pag4=pagina(3200,4)  

        self.contPag=[self.Pag1,self.Pag2,self.Pag3,self.Pag4]
    
    #LLena la memoria con los elementos adados y selecciona una pagina para introducir los elementos
    def llenarmemoria(self, elemento, peso,AP):
        sel=self.contPag[np.random.randint(0,4)]
        paginasel = sel.id
        aux=[]
        self.contadorid+=1
        aux.append(self.contadorid)
        aux.append(elemento)
        aux.append(peso)
        aux.append(paginasel)

        if self.capacidad-peso > 0:
            self.memoria.append(aux)
            sel.introducirpagina( aux,peso,self.contPag ,AP)
        else:
            return print("Memoria llena")

    #Borra la memoria con los elementos adados y selecciona una pagina para borrar los mismos
    def borrar(self,elemento,AP):
        idA=0
        idB=0

        for i in self.memoria:
            if elemento == i[1]:
                idA= i[3]
                idB= i[0]

                self.memoria.remove(i)
                break
        for j in self.contPag:
            if j.id == idA:
                j.borrarPagina(idB,AP)
        
    def escribir(self,elementoAct, elementoNuev,AP):
        idA=0
        idB=0
        for i in self.memoria:
            if elementoAct==i[1]:
                idA= i[3]
                idB= i[0]
                i[1]=elementoNuev
                break

        for j in self.contPag:
            if j.id == idA:
                j.escribirPagina(idB, elementoNuev,AP)


    def leer(self,elemento,AP):
        
        for i in self.memoria:
            if elemento==i[1]:
                print("Elemento leido: ",i[1], ", con id de pagina: ",i[3])
                AP.verificar(self.contPag[i[3]-1])
                AP.mostrar()
                break

        

#Inicia
def iniciar():

    memoria1=memoria(3200)
    AP = primario(2)
    return memoria1,AP

