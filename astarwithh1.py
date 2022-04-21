import copy


class a_star(object):
    def __init__(self):
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.tree = []
        self.i = 0

    def HEURISTIC_SEARCH(self, Start):
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
            NodeList = self.Sort_In(self.Successors(Node), NodeList)

    def Sort_In(self, sn, n):
        sn.extend(n)
        sn.sort(key=lambda x: x['f'])
        return sn

    def heuristic(self, x):
        h = 0
        for j in range(3):
            for k in range(3):
                if x[j][k] - self.goal[j][k] != 0 and self.goal[j][k] != 0:
                    h = h + 1
        return h

    def Successors(self, y):
        succ = []
        for j in range(3):
            for k in range(3):
                if y['State'][j][k] == 0:
                    if j >= 1:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j - 1, k)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.heuristic(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    if j < 2:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j + 1, k)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.heuristic(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    if k >= 1:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j, k - 1)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.heuristic(s['State'])
                            s['f'] = s['g'] + s['h']
                            s['Parent'] = y
                            succ.append(s)
                    if k < 2:
                        s = copy.deepcopy(y)
                        s['State'] = self.swap(s['State'], j, k, j, k + 1)
                        if s['State']:
                            s['g'] = y['g'] + 1
                            s['h'] = self.heuristic(s['State'])
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
    obj = a_star()
    Start = [{'State': [[2, 0, 4], [6, 7, 1], [8, 5, 3]], 'g': 0, 'h': 8, 'f': 8, 'Parent': None}]
    print(obj.HEURISTIC_SEARCH(Start))
    print('Number of iterations =', obj.i)
