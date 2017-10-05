# -*- coding: utf-8 -*-
from lettuce import step, world
from figuras import Figuras

@step(u'cuando calculo el area')
def cuando_calculo_el_area(step):
    pass

@step(u'Dado que ingreso el numero "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, radio):
	world.fig = Figuras()
	world.fig.circulo(int(radio))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.fig.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)


@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, base, altura):
    world.fig = Figuras()
    world.fig.triangulo(int(base), int(altura))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.fig.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'Dado que ingreso el lado "([^"]*)"')
def dado_que_ingreso_el_lado_group1(step, lado):
    world.fig = Figuras()
    world.fig.cuadrado(int(lado))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.fig.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'Dado que ingreso las medidas "([^"]*)" y "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_las_medidas_group1_y_group2_y_gruoup2(step, baseMay, baseMen, altura):
	world.fig = Figuras()
	world.fig.trapecio(int(baseMay), int(baseMen), int(altura))
@step(u'entonces obtengo el resultado "([^"]*)" y "([^"]*)" y "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.fig.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)