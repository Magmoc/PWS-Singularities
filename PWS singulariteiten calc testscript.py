# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:54:30 2019

@author: Erik
"""
#Importeer bibliotheken
#Zorg ervoor dat de bibliotheken geïnstalleerd zijn voor gebruik
#Gebruik Anaconda of pip. Zie internet voor meer uitleg
import sympy as sym
import datetime

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

#Functie om aantal singulariteiten te berekenen
def getSingularity(f):
   init_time = datetime.datetime.now()             #Begintijd
   
#  Berekent de partieel afgeleiden van de functie
   px = sym.Eq(sym.diff(f,x))
   py = sym.Eq(sym.diff(f,y))
   pz = sym.Eq(sym.diff(f,z))
   print("\nBeginnen met oplossen")
#   Lost de partieel afgeleiden op voor x, y en z op de versimpelde manier
   singList = sym.solve([px,py,pz,0],(x,y,z),minimal = True, simplify = False, rational = False)
   
#   Als het aantal singulariteiten minder is dan dat het zou moeten zijn, wordt alsnog de normale oplosmethode gebruikt
   if len(singList) < singCheck[sym.total_degree(f,x,y,z)-1]:
      singList = sym.solve([px,py,pz,0],(x,y,z))
   
#   Als er maar 1 singulariteit is is de output een dict. 
#   Als dat het geval is, wordt dat hier omgezet naar een lijst met een triple erin
#   dus [(x,y,z)]. Het is overigens niet nodig voor tweedegraadsvergelijkingen om
#   antwoorden te controleren, omdat het er maar één kan zijn.
   if isinstance(singList,dict):
      singList2 = [ v for v in singList.values() ]
      singList = [(singList2[0],singList2[1],singList2[2])]
   else:
#     Er wordt een kopie gemaakt van de antwoordenlijst, zodat elk antwoord wordt gecontroleerd
      singListcopy = singList.copy()
      
#      Hier worden alle gevonden "oplossingen" gecontroleerd door ze in te vullen in de vergelijking.
#      De "oplossingen" die niet voldoen worden eruit gehaald.
      print("Oplossingen gevonden. Oplossingen controleren...")
      for xans,yans,zans in singListcopy:
         fnew = rounddown(sym.simplify(f.subs([(x,xans),(y,yans),(z,zans)])))
         if fnew != 0:
            singList.remove((xans,yans,zans))
            
   new_time = datetime.datetime.now() #Eindtijd
   
#  De graad en de lengte van singList worden hier geprint.
#  Lengte van singList is dus het aantal singulariteiten
   print("d = ",sym.total_degree(f,x,y,z)," mu(f) = ",len(singList))
   
#  De tijd die het programma erover deed om het aantal singulariteiten van een bepaalde graad te berekenen
   print("Verstreken tijd: ", new_time-init_time,"\n")

x, y, z = sym.symbols('x y z', real=True) #x, y en z zijn nu variabelen
total_init_time = datetime.datetime.now() #Starttijd van het gehele script
print(total_init_time)

singCheck = [0,1,4,16,31,65] #Controlelijst met het aantal singulariteiten per graad

# Bereken het aantal singulariteiten van de volgende vergelijkingen:
# KEGEL
f = x**2 + y**2 - z**2
getSingularity(f)

#   CAYLEYS CUBIC
w = 1-x-y-z
f = y*z*w + x*z*w + x*y*w + x*y*z
getSingularity(f)

# KUMMERS QUARTIC MET MU^2 = 2
# MU^2 = 2/3 is niet meegenomen in het testscript, omdat we
# Alleen het maximum aantal wilde berekenen voor elke graad
w = 1
p = w-z-sym.sqrt(2)*x	
q =	w-z+sym.sqrt(2)*x	
r =	w+z+sym.sqrt(2)*y	
s =	w+z-sym.sqrt(2)*y
mu = 2
labda = (3*mu-1)/(3-mu) 
f = (x**2+y**2+z**2-mu*w**2)**2-labda*p*q*r*s 
getSingularity(f)

# TOGLIATIS QUINTIC
w = 1
f = (64*(x-w)*(x**4-4*x**3*w-10*x**2*y**2-4*x**2*w**2+16*x*w**3-20*x*y**2*w+5*y**4 + 16*w**4 - 20*y**2*w**2)
- (5*sym.sqrt(5-sym.sqrt(5)))*(2*z- sym.sqrt(5-sym.sqrt(5))*w)*(4*(x**2+y**2+z**2) + (1+ 3*sym.sqrt(5)*w**2))**2)
getSingularity(f)
  
# BARTHS SEXTIC
phi = 0.5*(1+sym.sqrt(5))
w = 0.25*(2 + sym.sqrt(5))
f = ((phi**2*x**2-y**2)*(phi**2*y**2-z**2)*(phi**2*z**2-x**2)
- w*(x**2+y**2+z**2- 1)**2)
getSingularity(f)

# LABS SEPTIC was heel lang en vertraagde Spyder. De eerste keer dat we het testprogramma uitvoerde zou
# tot en met de 6e graad berekend worden. Pas daarna zou de zevende graad berekend worden

total_new_time = datetime.datetime.now() #Eindtijd van het gehele script
print(total_new_time)
print("Totaal verstreken tijd: ", total_new_time - total_init_time)