import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    def __init__(self, x0, y0, v0, angle_deg, mass, time_step, max_time, drag_coefficient, cross_sectional_area):
        self.cross_sectional_area = cross_sectional_area
        self.max_time = max_time
        self.v0 = v0
        self.time_step = time_step
        self.drag_coefficient = drag_coefficient
        self.mass = mass
        self.angle_rad = np.radians(angle_deg)
        self.x = [x0]
        self.y = [y0]
        self.gravity = 9.81 
        self.air_density = 1.225  
        self.vx = [self.v0 * np.cos(self.angle_rad)]
        self.vy = [self.v0 * np.sin(self.angle_rad)]
        self.ax = [-abs(self.air_density * self.drag_coefficient * self.cross_sectional_area * (self.vx[-1])**2 / (2 * self.mass))]
        self.ay = [-self.gravity - abs(self.air_density * self.drag_coefficient * self.cross_sectional_area * (self.vy[-1])**2 / (2 * self.mass))]
    
    def euler_method(self):
        for _ in np.arange(0, self.max_time, self.time_step):
            self.x.append(self.x[-1] + (self.vx[-1] * self.time_step))
            self.y.append(self.y[-1] + (self.vy[-1] * self.time_step))
            self.vx[-1] += self.ax[-1] * self.time_step
            self.vy[-1] += self.ay[-1] * self.time_step
            self.ax = [-abs(self.air_density * self.drag_coefficient * self.cross_sectional_area * (self.vx[-1])**2 / (2 * self.mass))]
            self.ay = [-self.gravity - abs(self.air_density * self.drag_coefficient * self.cross_sectional_area * (self.vy[-1])**2 / (2 * self.mass))]
            if self.y[-1] < 0:
                break
    
    def runge_kutta_method(self):
        time_values = np.arange(0, self.max_time, self.time_step)
        for _ in time_values:
            kvx = [(-np.sign(self.vx[-1])*(self.air_density*self.drag_coefficient*self.cross_sectional_area/(2*self.mass))*(self.vx[-1])**2)*self.time_step]
            kvy = [((-self.gravity-np.sign(self.vy[-1])*(self.air_density*self.drag_coefficient*self.cross_sectional_area/(2*self.mass))*(self.vy[-1])**2)*self.time_step)]
            kx = [self.vx[-1]*self.time_step]
            ky = [self.vy[-1]*self.time_step]
            if self.y[-1] < 0:
                break

            for _ in range(len(time_values)-1):
                kvx.append((-np.sign(self.vx[-1])*(self.air_density*self.drag_coefficient*self.cross_sectional_area/(2*self.mass))*(self.vx[-1])**2)*self.time_step)
                kvy.append((-self.gravity-np.sign(self.vy[-1]+kvy[-1])*(self.air_density*self.drag_coefficient*self.cross_sectional_area/(2*self.mass))*(self.vy[-1]+kvy[-1])**2)*self.time_step)
                kx.append((self.vx[-1]+kvx[-1])*self.time_step)
                ky.append((self.vy[-1]+kvy[-1])*self.time_step)

            self.vx.append(self.vx[-1]+(kvx[0]+2*kvx[1]+2*kvx[2]+kvx[3])/6)
            self.vy.append(self.vy[-1]+(kvy[0]+2*kvy[1]+2*kvy[2]+kvy[3])/6)
            self.x.append(self.x[-1]+(kx[0]+2*kx[1]+2*kx[2]+kx[3])/6)
            self.y.append(self.y[-1]+(ky[0]+2*ky[1]+2*ky[2]+ky[3])/6)

    def get_info(self):
        print('Initial velocity: {}'.format(self.v0))
        print('Time step: {}'.format(self.time_step))
        print('Mass: {}'.format(self.mass))
        print('x coordinates: {}'.format(self.x)) 
        print('y coordinates: {}'.format(self.y))
        print('x velocity: {}'.format(self.vx))
        print('y velocity: {}'.format(self.vy))
        print('x acceleration: {}'.format(self.ax))
        print('y acceleration: {}'.format(self.ay))

    def plot_trajectory(self, method, show_plot=True):
        if method == 'euler':
            self.euler_method()
            plt.plot(self.x, self.y, label='Euler Method')
        elif method == 'runge_kutta':
            self.runge_kutta_method()
            plt.plot(self.x, self.y, label='Runge-Kutta Method')
        else:
            raise ValueError("Invalid method. Choose between 'euler' and 'runge_kutta'.")

        plt.title('Projectile Motion')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        if show_plot:
            plt.legend()
            plt.grid(True)
            plt.show()


p1 = Projectile(x0=0, y0=0, v0=50, angle_deg=45, mass=2, time_step=0.01, max_time=20, drag_coefficient=0.47, cross_sectional_area=0.02)
p2 = Projectile(x0=0, y0=0, v0=50, angle_deg=45, mass=2, time_step=0.001, max_time=20, drag_coefficient=0.47, cross_sectional_area=0.02)
p3 = Projectile(x0=0, y0=0, v0=50, angle_deg=45, mass=2, time_step=0.2, max_time=20, drag_coefficient=0.47, cross_sectional_area=0.02)
p4 = Projectile(x0=0, y0=0, v0=50, angle_deg=45, mass=2, time_step=0.01, max_time=20, drag_coefficient=0, cross_sectional_area=0.02)
p5 = Projectile(x0=0, y0=0, v0=50, angle_deg=45, mass=2, time_step=0.01, max_time=20, drag_coefficient=0.47, cross_sectional_area=0.02)

p1.plot_trajectory(method='euler', show_plot=False)
p2.plot_trajectory(method='euler', show_plot=False)
p3.plot_trajectory(method='euler', show_plot=False)
p4.plot_trajectory(method='euler', show_plot=False)
p5.plot_trajectory(method='runge_kutta', show_plot=False)

plt.legend(['dt = 0.01', 'dt = 0.001', 'dt = 0.2', 'dt = 0.01, Cd = 0', 'dt = 0.01, Runge-Kutta Method'])
plt.grid(True)
plt.show()
