def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def resolution(kb, query, visited=None):
    if visited is None:
        visited = set()
    if tuple(query) in visited:
        return False
    visited.add(tuple(query))

    for clause in kb:
        head = clause[0]
        tail = clause[1:]  
        theta = unify(head, query, {})
        if theta is not None:
            if not tail: 
                return True
          
            if all(resolution(kb, premise, visited) for premise in tail):
                return True
    return False

knowledge_base = [
    [["Mortal", "John"]],                 
    [["Human", "John"], ["Mortal", "John"]]  
]

query = ["Mortal", "John"]

if resolution(knowledge_base, query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")
