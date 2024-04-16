class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(v, x):
    if v is None:
        v = BSTNode(x)
    elif x < v.data:
        v.left = insert(v.left, x)
    elif x > v.data:
        v.right = insert(v.right, x)
    return v


def get(v, x):
    if v is None:
        return None
    if v.data == x:
        return v
    if x < v.data:
        return get(v.left, x)
    if x > v.data:
        return get(v.right, x)


def findmin(v):
    if v is None:
        return None
    if v.left is None:
        return v
    return findmin(v.left)


def remove(v, x):
    if v is None:
        return None
    if x < v.data:
        v.left = remove(v.left, x)
        return v
    if x > v.data:
        v.right = remove(v.right, x)
        return v
    if v.left is None:
        return v.right
    if v.right is None:
        return v.left

    u = findmin(v.right)
    v.data = u.data
    v.right = remove(v.right, u.data)

    return v

