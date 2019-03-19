from math import e, pi, log, sin, cos, tan

def f(x):
    return eval('x * (e ** x) - cos(x)')

def root(xi, xf, t = 16, step = 0):
    prev = xi
    xi = xf - ((f(xf) * (xf - xi)) / (f(xf) - f(xi)))

    if (str(prev)[:t + 2] == str(xi)[:t + 2]):
        return float(str(xi)[:t + 2]), step

    return root(xi, xi + 1, t, step + 1)

print(root(0.2, 1, 6))
