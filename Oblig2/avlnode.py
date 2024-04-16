class AVLNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


def get(v, x):
    if v is None:
        return None
    if v.data == x:
        return v
    if x < v.data:
        return get(v.left, x)
    if x > v.data:
        return get(v.right, x)


def height(v):
    h = -1
    if v is None:
        return h
    for u in [v.left, v.right]:
        h = max(h, height(u))
    return 1 + h


def leftrot(z):
    y = z.right
    t = y.left
    y.left = z
    z.right = t
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def rightrot(z):
    y = z.left
    t = y.right
    y.right = z
    z.left = t
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def balfac(v):
    if v is None:
        return 0
    return height(v.left) - height(v.right)


def balnace(v):
    if balfac(v) < -1:
        if balfac(v.right) > 0:
            v.right = rightrot(v.right)
        return leftrot(v)
    if balfac(v) > 1:
        if balfac(v.left) < 0:
            v.left = leftrot(v.left)
        return rightrot(v)

    return v


def insert(v, x):
    if v is None:
        v = AVLNode(x)
    elif x < v.data:
        v.left = insert(v.left, x)
    elif x > v.data:
        v.right = insert(v.right, x)
    v.height = 1 + max(height(v.left), height(v.right))

    return balnace(v)


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
    elif x > v.data:
        v.right = remove(v.right, x)
    elif v.left is None:
        v = v.right
        return v
    elif v.right is None:
        v = v.left
        return v
    else:
        u = findmin(v.right)
        v.data = u.data
        v.right = remove(v.right, u.data)

    v.height = 1 + max(height(v.left), height(v.right))

    return balnace(v)
