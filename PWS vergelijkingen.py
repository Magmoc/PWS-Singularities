# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:45:50 2019

@author: Erik
"""

# Dit zijn de vergelijkingen van de wereldrecordoppervlakken
# import sympy as sym

# 1e graad
# Vlak
# f = x + y +z

# 2e graad
# Kegel
# f = x**2 + y**2 - z**2

# 3e graad
# Cayleys Cubic
# w = 1-x-y-z
# f = y*z*w + x*z*w + x*y*w + x*y*z

# OF

# f = y*z*(1-x-y-z) + x*z*(1-x-y-z) + x*y*(1-x-y-z)  + x*y*z

# 4e graad
# Kummers Quartic
# mu = 2
# w = 1
# labda = (3*mu-1)/(3-mu) 
# p = w-z-sym.sqrt(2)*x	
# q =	w-z+sym.sqrt(2)*x	
# r =	w+z+sym.sqrt(2)*y	
# s =	w+z-sym.sqrt(2)*y
# f = (x**2+y**2+z**2-mu*w**2)**2-labda*p*q*r*s 

# 5e graad
# Togliatti Surface
# w = 1
# f = (64*(x-w)*(x**4-4*x**3*w-10*x**2*y**2-4*x**2*w**2+16*x*w**3-20*x*y**2*w+5*y**4 + 16*w**4 - 20*y**2*w**2) 
# - (5*sym.sqrt(5-sym.sqrt(5)))*(2*z- sym.sqrt(5-sym.sqrt(5))*w)*(4*(x**2+y**2+z**2) + (1+ 3*sym.sqrt(5)*w**2))**2)

# 6e graad
# Barth sextic
# phi = 0.5*(1+sym.sqrt(5))
# w = 0.25*(2 + sym.sqrt(5))
#   LABS
# f = ((phi**2*x**2-y**2)*(phi**2*y**2-z**2)*(phi**2*z**2-x**2) 
#       - w*(x**2+y**2+z**2- 1)**2)

# 7e graad
# Labs septic
# Te vinden in deze paper http://oliverlabs.net/wp-content/uploads/2018/04/AlgSurfManySings_English.pdf
# pagina 17