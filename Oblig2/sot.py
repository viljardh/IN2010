import avlnode

class Sot:
    def __init__(self):
        self.root = None
        self.larj = 0


def insert(set, x):
    if not avlnode.get(set.root, x):
        set.larj += 1
        set.root = avlnode.insert(set.root, x)


def remove(set, x):
    if avlnode.get(set.root, x):
        set.larj -= 1
        set.root = avlnode.remove(set.root, x)


def get(set, x):
    return avlnode.get(set.root, x)


def storr(set):
    return set.larj