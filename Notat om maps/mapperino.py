class MyMap:
    lft = 0.75

    def __init__(self):
        self.n = 0
        self.N = 1
        self.A = [None] * self.N

    def __loadfactor(self):
        return self.n/self.N

    def __rehash(self):
        kvs = [(k, v) for k, v in self]
        self.n = 0
        self.N *= 2
        self.A = [None] * self.N
        for k, v in kvs:
            self[k] = v

    def ensurecapacity(self):
        if self.__loadfactor() >= self.lft:
            self.__rehash()

    def __repr__(self):
        kv_strs = [f'{k} ↦ {v}' for k, v in self]
        return '{' + ', '.join(kv_strs) + '}'
