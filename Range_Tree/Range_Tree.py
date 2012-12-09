class r_node:
    ## n:sorting dimension l:list
    def __init__(self, l, n = 0):
        self.size = len(l)
        self.data = l
        if self.size == 1:
            self.r = 'NIL'
            self.l = 'NIL'
        else:
            self.r = r_node(l[:self.size / 2], n)
            self.l = r_node(l[self.size / 2:], n)

        if len(l[0]) == n + 1:
            self.next_dimension = 'NIL'
        else:
            self.next_dimension = r_node(sorted(l,key = lambda x:x[n + 1]), n + 1)

    def count(self, restrict, n = 0):
        if restrict[n][-1] < self.data[0][n] or self.data[-1][n] < restrict[n][0]:
            return 0
        elif restrict[n][0] <= self.data[0][n] and self.data[-1][n] <= restrict[n][-1]:
            if n + 1 == len(self.data[0]):
                return self.size
            else:
                return self.next_dimension.count(restrict, n + 1)
        else:
            return self.r.count(restrict, n) + self.l.count(restrict, n)
    
    def search(self, restrict,n = 0):
        if restrict[n][-1] < self.data[0][n] or self.data[-1][n] < restrict[n][0]:
            return []
        elif restrict[n][0] <= self.data[0][n] and self.data[-1][n] <= restrict[n][-1]:
            if n + 1 == len(self.data[0]):
                return self.data
            else:
                return self.next_dimension.search(restrict, n + 1)
        else:
            return self.r.search(restrict, n) + self.l.search(restrict, n)

class r_tree:
    ## d:dimension, l:list
    def __init__(self, l):
        self.d = len(l[0])
        if any(self.d != len(x) for x in l):
            return False
        self.root = r_node(sorted(l))
    
    def count(self, restrict):
        if len(restrict) != self.d:
            return False
        if any(len(x) != 2 for x in restrict):
            return False
        if any(x[0] > x[1] for x in restrict):
            return False
        return self.root.count(restrict)

    def search(self, restrict):
        if len(restrict) != self.d:
            return False
        if any(len(x) != 2 for x in restrict):
            return False
        if any(x[0] > x[1] for x in restrict):
            return False
        return self.root.search(restrict)
