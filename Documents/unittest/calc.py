def add(x,y):
    """Add Function"""
    return x + y

def subtract(x,y):
    """Subtract Function"""
    if x == 0:
        raise ValueError('can not have this value')
    return x - y