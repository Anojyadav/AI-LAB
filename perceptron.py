import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


class Perceptron():

    def __init__(self):
        self.n = 0
        self.a = ([8, 4, 1], [8, 6, 1], [9, 2, 1], [9, 5, 1])
        self.b = ([6, 1, 1], [7, 3, 1], [8, 2, 1], [9, 0, 1])
        self.w = ([1, 1, 1])


    def weight(self):

        while self.check() != len(self.a) + len(self.b):
            self.n = self.n + 1
            for i in range(len(self.a)):
                if np.dot(self.w, self.a[i]) <= 0:
                    self.w = np.add(self.w, self.a[i])

            for j in range(len(self.b)):
                if np.dot(self.w, self.b[j]) > 0:
                    self.w = np.subtract(self.w, self.b[j])

            print(self.w)
        print('No. of iterations =', self.n)
        for i in range(len(self.a)):
            plt.plot(self.a[i][0], self.a[i][1], 'o', color='green')
        for j in range(len(self.b)):
            plt.plot(self.b[j][0], self.b[j][1], 'o', color='red')
        x = np.linspace(np.min(self.b), np.max(self.a))
        plt.plot(x, (- self.w[2] - self.w[0] * x) / self.w[1])
        plt.show()

    def check(self):
        k = 0
        for i in range(len(self.a)):
            if np.dot(self.w, self.a[i]) > 0:
                k = k + 1
        for j in range(len(self.b)):
            if np.dot(self.w, self.b[j]) <= 0:
                k = k + 1
        return k


if __name__ == '__main__':
    obj = Perceptron()
    obj.weight()
