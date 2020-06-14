# Notes

## Pendulum

Harmonic equation

$X(t) = A \cdot sin(\frac{2\pi}{T}t)$

Where, $A$ is amplitude, $T$ is period, and $t$ is time. $X(t)$ is the position value at time $t$.

$X(t) = A \cdot sin(2\pi Ft)$ 

Where, $F$ is the frequency ($F = 1/T$).

https://techforcurious.website/simulation-of-pendulum-vpython-tutorial-visual-python/
![img](misc/pendulum.png)


## Numerical vs Analytical approach

The simplest breakdown would be this:

Analytical solutions can be obtained exactly with pencil and paper; 
Numerical solutions cannot be obtained exactly in finite time and typically cannot be solved using pencil and paper.

Question: find the root of $f(x) = x - 5$

Analytical solution: 
$f(x) = x - 5 = 0$, add +5 to both sides to get the answer $x = 5$.

Numerical solution:

let's guess $x=1$; $f(1) = 1-5 = 4$
let's guess $x=6$; $f(6) = 6-5 = 1$

Answer must be between. 

Numerical solutions are extremely abundant. The main reason is that sometimes we either don't have an analytical approach or that the analytical solution is too slow and instead of computing for 15 hours and getting an exact solution, we rather compute for 15 seconds and get a good approximation.

## Newtonian vs Lagrangian mechanics
https://physics.stackexchange.com/questions/8903/what-is-the-difference-between-newtonian-and-lagrangian-mechanics-in-a-nutshell


## Rohan Notes

equations of motion of the pendulum (taken from: https://arxiv.org/pdf/1902.10139.pdf)
```
def pendulum_dynamics(t,s,u):
    x, v, theta, omega = s
    
    dx = np.zeros(4) # [x_dot v_dot theta_dot omega_dot]
    
    dx[0] = v 
    dx[1] = u 
    dx[2] = omega
    dx[3] = np.sin(theta) - u*np.cos(theta)
    
    return dx
```
then you use Euler integration to propagate the states, i.e, x_{k+1} = x_{k} + dt*dx_k
(this is the simple way to propagate the dynamics)
given a certain initial condition x_i
and control inputs