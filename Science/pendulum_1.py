import numpy as np
from math import sin, cos
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def simplePendulumSimulation(theta0, omega0, dt, m, g, l, numSteps, plotFlag=False):
    # This function simulates a simple pendulum using the Euler-Cromer method.
    # Inputs: theta0 (the initial angle, in rad)
    #		  omega0 (the initial angular velocity, in rad/s)
    #		  dt (the time step)
    #		  m (mass of the pendulum)
    #	      g (gravitational constant)
    #		  l (length of the pendulum)
    #		  numSteps (number of time steps to take, in s)
    #	      plotFlag (set to 1 if you want plots, 0 otherwise)
    # Outputs: t_vec (the time vector)
    #		   theta_vec (the angle vector)

    # initialize vectors

    time_vec = [0]*numSteps
    theta_vec = [0]*numSteps
    omega_vec = [0]*numSteps
    KE_vec = [0]*numSteps
    PE_vec = [0]*numSteps

    # set initial conditions

    theta = theta0
    omega = omega0
    time = 0

    # begin time stepping

    for i in range(0, numSteps):

        omega_old = omega
        theta_old = theta
        # update the values
        omega = omega_old - (g/l)*sin(theta_old)*dt
        theta = theta_old + omega*dt
        # record the values
        time_vec[i] = dt*i
        theta_vec[i] = theta
        omega_vec[i] = omega
        KE_vec[i] = (1/2)*m*l**2*omega**2
        PE_vec[i] = m*g*l*(1-cos(theta))

    TE_vec = np.add(KE_vec, PE_vec)

    # make graphs

    if plotFlag:

        plt.figure(0)
        plt.plot(time_vec, theta_vec)
        plt.xlabel('Time (s)')
        plt.ylabel('Displacement (rad)')
        plt.savefig('plot1.png', bbox_inches='tight')

        # plt.figure(1)
        # plt.plot(time_vec, KE_vec, label='Kinetic Energy')
        # plt.plot(time_vec, PE_vec, label='Potential Energy')
        # plt.plot(time_vec, TE_vec, label='Total Energy')
        # plt.legend(loc='upper left')
        # plt.xlabel('Time (s)')
        # plt.ylabel('Energy (J)')
        # plt.savefig('plot2.png', bbox_inches='tight')

        # plt.figure(2)
        # plt.plot(theta_vec, omega_vec)
        # plt.xlabel('Displacement (rad)')
        # plt.ylabel('Velocity (rad/s)')
        # plt.savefig('plot3.png', bbox_inches='tight')

        # plt.show()

    return time_vec, theta_vec


dt = 0.01
L = 1
time_vec, theta_vec = simplePendulumSimulation(
    np.pi/6, 0, dt=dt, m=1, g=9.8, l=L, numSteps=500, plotFlag=True)

print(np.array(time_vec).shape)

fig = plt.figure()
lim = 1.5
ax = fig.add_subplot(111, autoscale_on=True, xlim=(-lim, lim), ylim=(-lim, lim))
ax.set_aspect('equal')
ax.grid()

ball_line, = ax.plot([], [], 'o-', lw=2, c='r')
thread_line, = ax.plot([], [], '-', lw=2)

time_template = 'time = %.3fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    ball_line.set_data([], [])
    thread_line.set_data([], [])
    time_text.set_text('')
    return thread_line, ball_line, time_text


def animate(i):
    x = L*sin(theta_vec[i])
    y = -L*cos(theta_vec[i])
    
    thread_line.set_data([0, x], [0, y])
    ball_line.set_data([x], [y])
    time_text.set_text(time_template % (i*dt))
    return thread_line, ball_line, time_text


ani = animation.FuncAnimation(fig, animate, np.arange(1, 500),
                              interval=25, blit=True, init_func=init,repeat=False)

plt.show()
