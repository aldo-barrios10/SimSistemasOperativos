import time 

#Este archivo tiene la asignacion del buffer

class buffer: 

    def __init__(self):
        self.cont=3072
        self.buffer=[]
        self.aux=[]

    #Agrega elementos a un buffer

    def agregar(self, id, dispositivo, tamano):
        if ((self.cont - tamano) > 0):
            self.aux=[]
            self.aux.append(id)
            self.aux.append(dispositivo)
            self.aux.append(tamano)
            self.buffer.append(self.aux)
            self.cont-=tamano
            return None
        else:
            print("Buffer lleno")


    #Elimina los elementos del buffer
    def eliminar(self):
        time.sleep(1)
        self.aux=self.buffer[0]
        aumento= self.aux[2]
        disp= self.aux[1]
        id= self.aux[0]
        del self.buffer[0]
        print("Se elimino el elemento con ID: ", id, " del dispositivo: ", disp, " y de memoria: ", aumento)
        print()
        self.cont+=aumento
        return None
        
    #Imprime el buffer (No se usa en el sist de archivos)
    def imprimir(self):
        print(self.buffer)
        
def inicia():
    buffer1=buffer()
    return buffer1

