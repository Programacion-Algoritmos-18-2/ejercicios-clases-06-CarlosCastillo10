"""
    @CarlosCastillo10
"""

import abc

class PersonaEquipo(metaclass=abc.ABCMeta): # Clase abstracta
    """
        se define la clases abstracta
    """
    __metaclass__ = abc.ABCMeta
    
    # Constructor
    def __init__(self, nom):
        self.nombre = nom

    # Metodo de agregar
    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    @abc.abstractmethod # Metodo abstracto
    def entrenar():
        pass


class Futbolista(PersonaEquipo): #Clase hija que hereda de (PersonaEquipo)
    
    # Constructor
    def __init__(self, n):
        super(Futbolista, self).__init__(n)
        self.posicion_campo = " "

    # Metodo de agregar
    def agregar_posicion_campo(self, p):
        self.posicion_campo = p

    # Metodo de obtener
    def obtener_posicion_campo(self):
        return self.posicion_campo

    # Metodo abstracto implementado
    def entrenar(self):
        print("Yo %s, futbolista, hago practica en el entrenamiento" % \
                self.nombre)


class Entrenador(PersonaEquipo): #Clase hija que hereda de (PersonaEquipo)
    
    # Constructor
    def __init__(self, n):
        super(Entrenador, self).__init__(n)
        self.codigo_entrenador = " "

    # Metodo de agregar
    def agregar_codigo_entrenador(self, c):
        self.codigo_entrenador = c

    # Metodo de obtener
    def obtener_codigo_entrenador(sefl):
        return codigo_entrenador
    
    # Metodo abstracto implementado
    def entrenar(self):
        print("Yo %s,entrenador, soy el director en el entrenamiento" % self.nombre)

class MedicoEquipo(PersonaEquipo): #Clase hija que hereda de (PersonaEquipo)
    
    # Constructor
    def __init__(self,n):
        super(MedicoEquipo,self).__init__(n)
        self.titulo = " "

    def agregar_titulo(self, t):
        self.titulo = t

    # Metodo de obtener
    def obtener_titulo(self):
        return self.titulo

    # Metodo abstracto implementado
    def entrenar(self):
        print("Yo %s, medico, atiendo a los jugadores en el entrenamiento" % self.nombre)
        

class PresidenteEquipo(PersonaEquipo): #Clase hija que hereda de (PersonaEquipo)
    
    # Constructor
    def __init__(self, n):
        super(PresidenteEquipo,self).__init__(n)
        self.numero_propiedades = 0

    # Metodo de agregar
    def agregar_numero_propiedades(self, num):
        self.numero_propiedades = num

    # Metodo de obtener
    def obtener_numero_propiedades(self):
        self.numero_propiedades

    # Metodo abstracto implementado
    def entrenar(self):
        print("Yo %s, presidente, pongo el dinero en el entrenamiento" % self.nombre)

        