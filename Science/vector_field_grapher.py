from __future__ import print_function
import numpy as np
import pylab as p

# Definition of parameters 


# def dX_dt(X, t=0):
#     """ Return the growth rate of fox and rabbit populations. """
#     a = 1.
#     b = 0.1
#     c = 1.5
#     d = 0.075
#     return array([ a*X[0] - b*X[0]*X[1] , -c*X[1] + d*X[0]*X[1] ])

def dX_dt(X, t=0):
    """ Simple ODE """
    a = 1.
    b = 2
    c = 3
    d = 4
    u, v = X

    '''
    eq. 1;
        du/dt = au + b
    eq. 2;
        dv/dt = cv + d
    '''
    return np.array([ a*u + b , -c*u*v + d ])

f2 = p.figure()

#-------------------------------------------------------
# define a grid and compute direction at each point
# ymax = p.ylim(ymin=0)[1]                        # get axis limits
# xmax = p.xlim(xmin=0)[1] 
ymax = 1.0
xmax = 1.0
nb_points   = 20                      

x = np.linspace(0, xmax, nb_points)
y = np.linspace(0, ymax, nb_points)

X1 , Y1  = np.meshgrid(x, y)                       # create a grid
DX1, DY1 = dX_dt([X1, Y1])                      # compute growth rate on the gridt
M = (np.hypot(DX1, DY1))                           # Norm of the growth rate 
M[ M == 0] = 1.                                 # Avoid zero division errors 
DX1 /= M                                        # Normalize each arrows
DY1 /= M                                  

#-------------------------------------------------------
p.title('Trajectories and direction fields')
p.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=p.cm.jet)
p.xlabel('Number of #')
p.ylabel('Number of #')
p.legend()
p.grid()
p.xlim(0, xmax)
p.ylim(0, ymax)
f2.savefig('vector_field_grapher.png')

p.show()