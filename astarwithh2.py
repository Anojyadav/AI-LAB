import copy


class Astar():
    def __init__(self):
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.tree = []
        self.i = 0

    def heuristic_search(self, Start):
        NodeList = Start
        while True:
            self.i = self.i + 1
            if not NodeList:
                return 'No solution'
            Node = NodeList[0]
            self.tree.append(Node['State'])
            NodeList = NodeList[1:]
            if Node["State"] == self.goal:
                return 'Solution found', Node
            NodeList = self.sort_in(self.successors(Node), NodeList)

    def sort_in(self, sn, n):
        sn.extend(n)
        sn.sort(key=lambda x: x['f'])
        return sn

    def manhat(self, w):
        h = 0
        for j in range(3):
            for k in range(3):
                if w[j][k] == 1:
                    h = h + j + k
                elif w[j][k] == 2:
                    h = h + j + abs(k - 1)
                elif w[j][k] == 3:
                    h = h + j + 2 - k
                elif w[j][k] == 4:
                    h = h + abs(j - 1) + k
                elif w[j][k] == 5:
                    h = h + abs(j - 1) + abs(k - 1)
                elif w[j][k] == 6:
                    h = h + abs(j - 1) + 2 - k
                elif w[j][k] == 7:
                    h = h + 2 - j + k
                elif w[j][k] == 8:
                    h = h + 2 - j + abs(k - 1)
        return h

    def successors(self, y):
        succ = []
        for j in range(3):
            for k in range(3):
                if y['State'][j][k] == 0:
                    if j >= 1:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j - 1, k)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.manhat(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    if j < 2:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j + 1, k)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.manhat(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    if k >= 1:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j, k - 1)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.manhat(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    if k < 2:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j, k + 1)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.manhat(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    return succ

    def swap(self, z, a, b, c, d):
        e = z[c][d]
        z[c][d] = z[a][b]
        z[a][b] = e
        if z in self.tree:
            return []
        else:
            return z


if __name__ == '__main__':
    obj = Astar()
    start = [{'State': [[6, 4, 7], [8, 5, 0], [3, 2, 1]], 'g': 0, 'h': 8, 'f': 8, 'Parent': None}]
    print(obj.heuristic_search(start))
    print('Number of iterations =', obj.i)
