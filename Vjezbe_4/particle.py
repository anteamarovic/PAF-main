import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, kut, x, y):
        self.v0 = v0
        self.kut = kut
        self.x = x
        self.y = y
        self.vx = self.v0 * math.cos(self.kut * (math.pi / 180))
        self.vy = self.v0 * math.sin(self.kut * (math.pi / 180))
        self.listax = [self.x]
        self.listay = [self.y]
        self.xx = x
        self.yy = y
        self.vv = v0
        self.vxx = self.vx
        self.vyy = self.vy

    def printinfo(self):
        print('brzina čestice je', self.v0)
        print('kut oklona čestice je ', self.kut)
        print('položaj čestice je ', self.x, self.y)
        print('brzine x i y ', self.vx, self.vy)

    def reset(self):
        self.v0 = self.vv
        self.x = self.xx
        self.y = self.yy
        self.vx = self.vxx
        self.vy = self.vyy

    def __move(self, t):
        ax = 0
        ay = -9.81
        self.vx = self.vx + ax * t
        self.y = self.y + self.vy * t
        self.vy = self.vy + ay * t
        self.x = self.x + self.vx * t

        return self.x, self.y

    def domet(self, t):
        while self.y >= 0:
            self.__move(t)
        return self.x

    def plot_trajectory(self, t):
        self.reset()
        while self.y >= 0:
            self.__move(t)
            self.listax.append(self.x)
            self.listay.append(self.y)
        plt.plot(self.listax, self.listay)
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.title('Trajectory of the particle')
        plt.grid(True)
        plt.show()


p1 = Particle(10, 45, 0, 0)
p1.plot_trajectory(0.1)  
