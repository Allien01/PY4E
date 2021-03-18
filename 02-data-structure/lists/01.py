def chop(t):  # remove o primeiro e último elemento de uma lista
    del t[0]
    del t[-1]
    return None


def middle(t2):  # recebe uma lista e retorna uma nova lista
    chop(t2)
    return t2

x = [1, 3, 4, 5, 2, 3, 4]
print(middle(x))
