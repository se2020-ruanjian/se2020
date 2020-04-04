import math
from math import fabs
from math import pi

def sin_se_p(angle):
    x = (angle/180)*pi;
    g = 0
    t = x
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return g

#ans = sin_se_p(pi / 2)
#print(ans)
#print( math.sin(pi / 2) )
