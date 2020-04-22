import math 
from math import pi

def cos_se_p(angle):
    x = (angle/180)*pi;
    cosTotal  = 1
    count = 2
    term = 1
    x=float(x) 
    while abs(term) > 1e-20:
        term *= (-x * x)/( count * (count-1) )   
        cosTotal += term
        count += 2
        #print("%1d  %22.17e" % (count, term))
    return cosTotal

#print( cos_se_p(0) )
#print( math.cos(0) )