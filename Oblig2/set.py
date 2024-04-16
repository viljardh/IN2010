import bstnode

class Set:
    def __init__(self):
        self.root = None
        self.larj = 0


def insert(set, x):
    if not bstnode.get(set.root, x):
        set.larj += 1
        set.root = bstnode.insert(set.root, x)


def remove(set, x):
    if bstnode.get(set.root, x):
        set.larj -= 1
        set.root = bstnode.remove(set.root, x)


def get(set, x):
    return bstnode.get(set.root, x)


def storr(set):
    return set.larj