
#Este archivo contiene la asignación de memoria cache y sus niveles

class memoria:
    def __init__(self, id,tamano):
        self.id= id
        self.tamano = tamano
        self.almacenamiento = []

    #Agrega elementos aun amemoria
    def agregar(self, elemento, peso, contador):
        aux= []
        if self.tamano - peso >= 0:
            aux.append(contador)
            aux.append(elemento)
            aux.append(peso) 
            self.almacenamiento.append(aux) 
            self.tamano-=peso

    #Busca los elementos en una memoria
    def buscar(self,elemento):
        existe = False
        for e in self.almacenamiento:
            if e[1] == elemento:
                existe= True
                return existe, e
        return existe, 0
        
#Verifica si existe el elemnto en cada una de las memorias
def ejecutar(elemento,contador, peso, memorias):
    mem=memorias[0]
    existe, e=mem.buscar(elemento) #Registro del procesador
    if existe:
        return e

    mem=memorias[1]
    existe, e=mem.buscar(elemento)# L1
    if existe:
      return e
    
    mem=memorias[2]
    existe, e=mem.buscar(elemento)#L2
    if existe:
      return e
    
    mem=memorias[3]
    existe, e=mem.buscar(elemento)#L3
    if existe:
      return e

    mem=memorias[4]
    existe, e=mem.buscar(elemento)#RAM
    if existe:
      return e

    #Si no existe entonces se trata de insertar

    #Caso de memoria RAM llena
    if mem.tamano == 0:
        for j in memorias:
            aux=[contador,elemento, peso]
            j.almacenamiento.pop()
            j.almacenamiento.insert(0,aux)

    #Otro caso
    for j in memorias:
        j.agregar(elemento,peso,contador)

    #Se busca nuevamente 
    mem=memorias[4]
    existe, e = mem.buscar(elemento)
    return e


def iniciar():
    rp=memoria(0,2)
    l1=memoria(0,3)
    l2=memoria(0,4)
    l3=memoria(0,5)
    ram=memoria(0,6)
    contador= 0

    listamem= [rp,l1,l2,l3,ram]

    return listamem
