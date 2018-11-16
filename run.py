#Autor: Carlos Castillo

from mipaquete.modelo import * # Importamos de mi paquete.modelo todo


futbolista = Futbolista("Antonio") # Creamos el objeto de tipo Futbolista
medico = MedicoEquipo("Ramon") # Creamos el objeto de tipo MedicoEquipo
presidente = PresidenteEquipo("Francisco") # Creamos el objeto de tipo Presidente
entrenador = Entrenador("Jose") # Creamos el objeto de tipo Entrenador

lista = [futbolista, medico, presidente, entrenador] #Guardamos en la lista los objetos

for l in lista:
	l.entrenar() #Presentamos el metodo entrenar de cada objeto.

