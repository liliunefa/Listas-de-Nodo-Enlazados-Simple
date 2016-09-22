VER: https://repl.it/DfRN/1
# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelante de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info
			nodo=nodo.sig
			
	# Metodo para mostrar si hay elementos repetidos
	def repetidos (self):
		iguales = False
		comparar = self
		nodo_comparar = comparar.__primero
		for i in range (comparar.__n):
			nodo = self.__primero
			for j in range (self.__n):
				if(i!=j and nodo_comparar.info==nodo.info):
					iguales = True
				nodo=nodo.sig
			nodo_comparar=nodo_comparar.sig
		print iguales#retorna True si hay elementos repetidos
		
	# Metodo para comparar dos listas
	def comparar (self,comparar):
		iguales = True
		nodo_comparar = comparar.__primero
		nodo = self.__primero
		for i in range (comparar.__n):
			if(nodo_comparar.info!=nodo.info):
				return False
			nodo=nodo.sig
			nodo_comparar=nodo_comparar.sig
		return iguales#retorna True si hay elementos iguales
		
	# Metodo para saber si los elementos estan ordenados (recibe por parametro si se comprueba
	# que se odene ascendente o descendente)
	def ordenados (self,asc):
		orden = True
		nodo = self.__primero
		siguiente = nodo.sig
		for i in range (self.__n):
			if siguiente!=None:
				# Si es ascendente
				if asc:
					print nodo.info,'<',siguiente.info
					if(nodo.info>siguiente.info):
						orden = False
				# Si es descendente
				else:
					print nodo.info,'>',siguiente.info
					if(nodo.info<siguiente.info):
						orden = False
					
				siguiente=siguiente.sig
			nodo = nodo.sig				
		return orden#retorna True si los elementos estan ordenados
			
	# Metodo para saber si los elementos son consecutivos
	## El parametro elementos corresponde al numero de consecusiones (si es de 1 en 1, de 2 en 2)
	def consecutivos (self,elementos=1):
		con = True
		nodo = self.__primero
		siguiente = nodo.sig
		for i in range (self.__n):
			if siguiente!=None:
				if(nodo.info+elementos!=siguiente.info):
					con = False
				siguiente=siguiente.sig
			nodo = nodo.sig				
		return con#retorna True si los elementos estan consecutivos
		
	# Metodo para sumar los enteros de una lista
	def suma_enteros (self):
		suma = 0
		nodo = self.__primero
		for i in range (self.__n):
			if(type(nodo.info)==int):
				suma += nodo.info
			nodo = nodo.sig				
		return suma#retorna la suma de los elementos
			
			
	# Metodo pos_actual	
			
	def pos_actual (self, pos):

		nodo  = self.__primero
		cont = 0
		while (nodo != None) :
			
			if (cont == pos):
				self.__actual=nodo
				self.__actual=pos
				self.__pos=cont
				print self.__actual
			
			nodo = nodo.sig
			cont=cont+1
		return
		

	# Metodo para mostrar la posicion actual 
	def buscar_elem (self,valor):
		nodo = self.__primero
		while(nodo!=None):
			if(nodo.info==valor):
				return True
			nodo=nodo.sig
		return False
		
	# Metodo para eliminar el primero
	def eliminar_primero(self):
		if (self.__primero==None):
			return
		nodo=self.__primero
		self.__primero=nodo.sig
		self.__n=self.__n-1
		self.__pos=self.__pos-1
		del nodo
		if (self.__n==0):
			self.__ultimo=None
			self.__actual=None

			
# PRINCIPAL 

# Crea la lista de elementos
l = Lista()

# Inserta elementos en la lista 
l.insertar_actual(5);
l.insertar_actual(10);
l.insertar_actual(15);
l.insertar_actual(20);
#l.insertar_inicio(25);
#l.insertar_actual(30);
#l.insertar_ultimo(35);

# Muestra los elementos de la lista 
l.mostrar()
if (l.buscar_elem(15) == True):
	print "lo encontro"
else:
	print "no lo encontro"
l.eliminar_primero()
l.mostrar()
l.pos_actual(3)
l.mostrar()
#Si retorna True hay uno o mas elementos iguales, de lo contrario falso
l.repetidos()
#Se crea otra lista para probar
otra_lista = Lista()
otra_lista.insertar_actual(5);
otra_lista.insertar_actual(10);
otra_lista.insertar_actual(15);
otra_lista.insertar_actual(20);
otra_lista.insertar_inicio(25);
otra_lista.insertar_actual(30);
otra_lista.insertar_ultimo(35);
#Si retorna True las listas son iguales, de lo contrario Falso
l.comparar(otra_lista)
l.ordenados(True)
print l.consecutivos()
print l.suma_enteros()

