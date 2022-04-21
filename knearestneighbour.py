import matplotlib.pyplot as plt
import random


class KNN():
    def __init__(self):
        self.a = [{'x': 6, 'y': 1, 'class': 0, 'dist': 0}, {'x': 7, 'y': 3, 'class': 0, 'dist': 0},
                  {'x': 8, 'y': 2, 'class': 0, 'dist': 0},
                  {'x': 9, 'y': 0, 'class': 0, 'dist': 0}, {'x': 8, 'y': 4, 'class': 1, 'dist': 0},
                  {'x': 8, 'y': 6, 'class': 1, 'dist': 0}, {'x': 9, 'y': 2, 'class': 1, 'dist': 0},
                  {'x': 9, 'y': 5, 'class': 1, 'dist': 0}]
        self.p = {'x': 8, 'y': 3.5, 'class': None}
        self.k = 7
        self.count_class_0 = 0
        self.count_class_1 = 0

    def k_nearest_neighbour(self):
        for i in range(len(self.a)):
            self.a[i]['dist'] = abs(self.a[i]['x'] - self.p['x']) + abs(self.a[i]['y'] - self.p['y'])
            if self.a[i]['class'] == 0:
                plt.plot(self.a[i]['x'], self.a[i]['y'], 'o', color='red')
            else:
                plt.plot(self.a[i]['x'], self.a[i]['y'], 'o', color='green')
        self.a.sort(key=lambda x: x['dist'])
        for j in range(self.k):
            if self.a[j]['class'] == 0:
                self.count_class_0 = self.count_class_0 + 1
            if self.a[j]['class'] == 1:
                self.count_class_1 = self.count_class_1 + 1
            print(j + 1, 'nearest neighbour =', self.a[j])
        print('class_count_0 =', self.count_class_0)
        print('class_count_1 =', self.count_class_1)
        if self.count_class_1 > self.count_class_0:
            self.p['class'] = 1
        elif self.count_class_1 < self.count_class_0:
            self.p['class'] = 0
        else:
            self.p['class'] = random.randint(0, 1)
        if self.p['class'] == 0:
            plt.plot(self.p['x'], self.p['y'], '^', color='red')
        else:
            plt.plot(self.p['x'], self.p['y'], '^', color='green')
        print('point =', self.p)
        plt.show()


if __name__ == '__main__':
    obj = KNN()
    obj.k_nearest_neighbour()
