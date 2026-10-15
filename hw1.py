# Name: Kathy Zeng
# hw1.py for part (b) through (e)

def TREE_HEIGHT(TREE):
    """
    args: TREE which is type tuple
    Return the height of the tree using recursion
    """
    label, children = TREE

    if not children:
        return 0

    return 1 + max(TREE_HEIGHT(child) for child in children)

def BRANCHING_FACTOR(TREE):
    """
    args: TREE which is type tuple
    Returns maximum branching factors 
    """

    children = TREE[1] 

    if not children:
        return 0

    return max(len(children), max(BRANCHING_FACTOR(child) for child in children))

def DFS_ORDER(TREE, GOALS):
    '''
    args:
    TREE: TREE which is type tuple
    GOALS: a node that makes the search terminates.
    Return a tuple of labels 
    '''
    
    order = []

    def search(node):
        if not node:
            return False

        root, children = node
        order.append(root)

        if root in GOALS:
            return True

        for child in children:
            if search (child):
                return True
        return False

    search(TREE)

    return tuple(order)
    
def DLS_ORDER(TREE, GOALS, LIMIT):
    """
    TREE: TREE which is type tuple
    GOALS: a node that makes the search terminates.
    LIMIT: limit the iteration
    """

    order = []

    def search(node, depth):
        label, children = node
        order.append(label)

        if label in GOALS:
            return True

        if depth == LIMIT:
            return False

        for child in children:
            if search(child, depth + 1):
                return True

        return False

    found = search(TREE, 0)
    return (tuple(order), found)

def IDS_ORDER(TREE, GOALS):
    """
    TREE: TREE which is type tuple
    GOALS: a node that makes the search terminates.
    """

    result = []

    for limit in range(TREE_HEIGHT(TREE) + 1):
        order, found = DLS_ORDER(TREE, GOALS, limit)
        result.append(order)

        if found:
            break

    return tuple(result)

T = ("A", (
    ("B", (("E", (("I", ()),)), ("F", ()))),
    ("C", (("G", ()),)),
    ("D", (("H", ()),))
    ))

print("The tree height is", TREE_HEIGHT(T) )
print("The branching factor is",BRANCHING_FACTOR(T) )

print("The ordering is ", DFS_ORDER(T, ("I", "G"))  )
print(DLS_ORDER(T, ("M",), 0) )
print(DLS_ORDER(T, ("R",), 0) )
print(IDS_ORDER(T, ("M",)) )

print()

U = ("R", (("L", ()), ("M", ())))
print(TREE_HEIGHT(U))
print(BRANCHING_FACTOR(U))

print("The ordering is", DFS_ORDER(U, ('M',)))
print(DLS_ORDER(U, ("M",), 0) )
print(DLS_ORDER(U, ("R",), 0) )
print(IDS_ORDER(U, ("M",)) )

W = ("A", (
    ("B", (
        ("D", (
            ("E", ()),
        )),
    )),
    ("C", ())
))
print()
print("The tree height is", TREE_HEIGHT(W) )
print("The branching factor is",BRANCHING_FACTOR(W) )
print(DFS_ORDER(W, ("E", "C")) )
print(IDS_ORDER(W, ("E", "C")) )
print()
print(IDS_ORDER(W, ("E",)))
print(DLS_ORDER(W, ("E",), 4))
print()

print(DLS_ORDER(W, ("X",), 4))
print()

U = ("A", ())
print("The tree height is", TREE_HEIGHT(U) )
print("The branching factor is",BRANCHING_FACTOR(U) )
print(DFS_ORDER(U, ("A")) )
print(IDS_ORDER(U, ("A")) )
print(DLS_ORDER(U, ("A",), 0))
print()

