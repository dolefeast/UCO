import sympy as sp
from sympy.utilities.lambdify import lambdify
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan, log
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


#for letter in abc:
#    exec("%s = '%s'" % (letter, letter)) #Defines variables a = 'a', b = 'b', etc

def set_size(width_pt, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to sit nicely in our document.

    Parameters
    ----------
    width_pt: float
            Document width in points
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


df = pd.read_excel('fresnel.ods') #The dataframe we're working on


for column in df.columns:
    exec("%s = df['%s']" % (column, column)) #This creates a variable with the name of the column and assigns it every value of the variable


#print(dtheta_i)
#X, Y, Z, T = sp.symbols('X, Y, Z, T')
#variables = [X, Y, Z, T] 
#dX, dY, dZ, dT = sp.symbols('dX, dY, dZ, dT')
#dvariables = [dX, dY, dZ, dT] #Los errores de las magnitudes. Tendré que apañármelas para conseguirlas del excel
#
#g = theta_i + phi
#f = lambdify(variables, g)
#dgsquared = lambdify([variables, dvariables], sum([diff(g, var)**2 * dvar**2 for var in variables for dvar in dvariables]))
#
#errors = []
#He decidido no hacer esto

#Plotting tests
fig, ax = plt.subplots(2, 2, figsize=set_size(345))
ax[0,0].set_title('Ángulos')
ax[0,0].errorbar(theta_i, phi, dtheta_i, dphi, fmt='o-', label=r'$\theta$', elinewidth=0.5)
ax[0,0].legend(loc='best')
#ax[0].plot(theta_i, psi_teo, 'o-', label=r'$\theta_i$ frente a $\psi_teórico$ ') 
ax[1,0].plot(theta_i, rho, 'o-')
plt.savefig('histogram.pgf')
#print(plt.legend.__doc__)
plt.show()
