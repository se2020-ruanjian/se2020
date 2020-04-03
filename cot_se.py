import math
from math import fabs
from math import pi

def cot_se_p(angle):
    x = (angle/180)*pi;
    x1 = float(x)
    x2 = float(x)
    g = 0
    t = x1
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x1 * x1 / (2 * n - 1) / (2 * n - 2)   #sin

    cosTotal  = 1
    count = 2
    term = 1
    #x=float(x) 
    while abs(term) > 1e-20:
        term *= (-x2 * x2)/( count * (count-1) )   
        cosTotal += term
        count += 2                                   #cos
        #print("%1d  %22.17e" % (count, term))
    g = cosTotal/g
    return g