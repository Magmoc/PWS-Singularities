# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:54:30 2019

@author: Erik
"""

#Deze bibliotheken worden geïmporteerd zodat ze gebruikt kunnen worden
#Zorg ervoor dat matplotlib, sympy en numpy geïnstalleerd zijn
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import sympy as sym

#e is de variabele die de vergelijking bevat
e = "y*z*(1-x-y-z) + x*z*(1-x-y-z) + x*y*(1-x-y-z)  + x*y*z"

#Er wordt een plot gemaakt en het wordt in volledig scherm weergegeven
#SPYDER: Zorg ervoor dat 
#Tools>Preferences>iPython console>Graphics>Graphics backend>Automatic
#Anders wordt het plot klein weergegeven
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(top=0.979, bottom=0.021, left=0.011, right=0.989, hspace=0.2, wspace=0.2)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

#De functie om een vergelijking te plotten
def plot_implicit(bbox=(-5, 5)):
    ax.clear()  #Als eerste wordt het plot leeggemaakt, zodat er nieuwe figuren kunnen worden geplot
    x, y, z = sym.symbols('x y z', real=True)   #x, y en z zijn de variabelen
    xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3  #De afmetingen van het plot worden bepaald
    A = np.linspace(xmin, xmax, 100)  #resolutie van de contour
    B = np.linspace(xmin, xmax, 15)  #Aantal lagen
    A1, A2 = np.meshgrid(A, A)  #Meshgrid/Rooster waarop de contour wordt geplot

    for z in B:  # plot contouren in xy-vlakken
        X, Y = A1, A2
        Z = Eq(X, Y, z)
        ax.contour(X, Y, Z + z, [z], zdir='z')
#         [z] bepaalt dat alleen voor deze waarde van z het contour geplot moet worden
#         Oftewel F(x,y,z) wordt gelijkgesteld aan 0

    for y in B:  # plot contouren in xz-vlakken
        X, Z = A1, A2
        Y = Eq(X, y, Z)
        ax.contour(X, Y + y, Z, [y], zdir='y')

    for x in B:  # plot contouren in yz-vlakken
        Y, Z = A1, A2
        X = Eq(x, Y, Z)
        ax.contour(X + x, Y, Z, [x], zdir='x')

#    De limieten worden ingesteld voor de assen
    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
    
#    De assen worden gelabeld
    ax.set_xlabel('x-as')
    ax.set_ylabel('y-as')
    ax.set_zlabel('z-as')
    
#    Het plot wordt getoond
    plt.show()

def Eq(xinp, yinp, zinp): #De functie om waarden van de vergelijking te berekenen
    x, y, z = xinp, yinp, zinp #De x, y en z worden nu gelijkgesteld aan de inputwaarden
    return eval(e) #Het geeft de evaluatie van de vergelijking terug
 
#    Eval neemt als input een string (een stuk tekst) en 
#    vult alle variabelen die gevonden kunnen worden in in de tekst
#    Daarna wordt het versimpeld en wordt er dus een waarde berekend
#    Voorbeeld:
#       Vergelijking = "2*x + y - z"
#       x, y, z = 3, 4, 6
#       eval(Vergelijking) 
#       Out: 4
#    Er wordt hier gebruik gemaakt van eval() omdat de invoer
#    van de invoerbalk wordt gezien als string en niet als vergelijking

def getEq(einp): #De functie die wordt geroepen wanneer er nieuwe tekst in de invoerbalk wordt gezet
   
#  e is globale variabele. Het is overal beschikbaar
   global e
   
   e = einp #Invoervergelijking wordt nu de vergelijking van e
   
#   Nieuwe vergelijking wordt geplot
   plot_implicit() 
   plt.draw()

#Er wordt een invoerbalk gemaakt en bij nieuwe invoer wordt het plot geüpdated
axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, label='Vergelijking:', initial=e)
text_box.on_submit(lambda eq: getEq(eq))

#Vergelijking wordt geplot
plot_implicit()