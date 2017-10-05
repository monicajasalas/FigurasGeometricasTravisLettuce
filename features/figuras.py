# -*- coding: utf-8 -*-

class Figuras(object):
	def __init__(self):
		self.resultado = 0

	def circulo(self, radio):
		
		try:
			if radio <= 0:
				return 'No se aceptan 0s'

			else:
				pi = 3.1416
				radio = int(radio)
				self.resultado = pi * (radio**2)
				self.resultado = round(self.resultado, 0)
		except:
			return 'Dato Incorrecto'

	def triangulo(self, base, altura):

		try:

			if altura <=0 or base <=0:
				return 'No se aceptan 0s'

			else:
				base = int(base)
				altura = int(altura)
				self.resultado = (base * altura) / 2
		except:
			return 'Dato Incorrecto'

	def cuadrado(self, lado):

		try:

			if lado <= 0:
				return 'No se aceptan 0s'
				
			else:
				lado = int(lado)
				self.resultado = lado * lado

		except:
			return 'Dato Incorrecto'

	def trapecio(self, baseMay, baseMen, altura):

		try:

			if baseMay <= 0 or baseMen <=0 or altura <=0:
				return 'No se aceptan 0s'

			else:
				baseMay = int(baseMay)
				baseMen = int (baseMen)
				altura = int(altura)
				self.resultado = ((int(baseMay) + int(baseMen))) * altura /  2

		except:
			return 'Dato Incorrecto'



	def obtener_resultado(self):
		return self.resultado