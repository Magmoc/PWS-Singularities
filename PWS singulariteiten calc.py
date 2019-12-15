# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:54:30 2019

@author: Erik
"""

#Importeer bibliotheken
import sympy as sym
 
#Functie om getallen als 1.634e-16 af te ronden naar 0
#(Sympy laat soms dit soort hele kleine getallen staan door de manier waarop het berekeningen uitvoert
#terwijl het antwoord wel 0 zou moeten zijn)
#Het kijkt in de vergelijking of een onderdeel een float (kommagetal) is. Zo ja rond het het af op 4 decimalen
def rounddown(eq):
   ex2 = eq
   for a in sym.preorder_traversal(eq):
      if isinstance(a, sym.Float):
         ex2 = ex2.subs(a, round(a, 4))
   return ex2

def getSingularity(f):
   x, y, z = sym.symbols('x y z', real=True)       #x, y en z zijn nu variabelen
   
#   Als de vergelijking een string is, wordt deze omgezet naar een vergelijking 
#   en worden de partieel afgeleiden bepaald
#   Dit is nodig als getSingularity(f) gebruikt wordt bij het plotten van figuren
#   De invoer van het plotten van figuren is namelijk een string. 
#   Dus moet deze omgezet worden
   if isinstance(f,str):
      ns = {"x" : sym.Symbol('x',real=True),
            "y" : sym.Symbol('y',real=True),
            "z" : sym.Symbol('z',real=True)}
      f = sym.sympify(f, locals = ns)
      px = sym.diff(f,x)
      py = sym.diff(f,y)
      pz = sym.diff(f,z)
   else:
#     Berekent de partieel afgeleiden van de functie
      px = sym.Eq(sym.diff(f,x))
      py = sym.Eq(sym.diff(f,y))
      pz = sym.Eq(sym.diff(f,z))
#   Lost de partieel afgeleiden op voor x, y en z op de versimpelde manier
   singList = sym.solve([px,py,pz,0],(x,y,z),minimal = True, simplify = False, rational = False)
   
#   Als er geen antwoorden komen met de versimpelde manier, wordt alsnog de normale oplosmethode gebruikt
   if len(singList) == 0:
      singList = sym.solve([px,py,pz,0],(x,y,z))
   
#   Als er maar 1 singulariteit is is de output een dict. 
#   Als dat het geval is, wordt dat hier omgezet naar een lijst met een triple erin
#   dus [(x,y,z)]
   if isinstance(singList,dict):
      singList2 = [ v for v in singList.values() ]
      singList = [(singList2[0],singList2[1],singList2[2])]
   else:
      singList2 = singList.copy()
      
#      Hier worden alle gevonden "oplossingen" gecontroleerd door ze in te vullen in de vergelijking.
#      De "oplossingen" die niet voldoen worden eruit gehaald.
      for xans,yans,zans in singList2:
         fnew = rounddown(sym.simplify(f.subs([(x,xans),(y,yans),(z,zans)])))
         if fnew != 0:
            singList.remove((xans,yans,zans))
   
#  De singList is de output
   return singList