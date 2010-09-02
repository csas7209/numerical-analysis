#!/usr/bin/env python

# This code was originally written by Zahir Jacobs:
# http://zahirj.wordpress.com/2009/04/04/complete-listing-of-python-code-for-selected-root-finding-methods/

import math
from helpers import *

def mullers_method(func, a, b, r, max_steps=MaxSteps):
    print_header("Muller's method", func)
    x = [a,b,r]
    for loopCount in range(max_steps):
        x = swap_points(x)
        y = evaluate(func,float(x[0])),evaluate(func,float(x[1])),evaluate(func,float(x[2]))
        h1 = x[1]-x[0]
        h2 = x[0]-x[2]
        lam = h2/h1
        c = y[0]
        a = (lam*y[1] - y[0]*((1.0+lam))+y[2])/(lam*h1**2.0*(1+lam))
        b = (y[1] - y[0] - a*((h1)**2.0))/(h1)
        if b > 0:
            root = x[0] - ((2.0*c)/(b+ (b**2 - 4.0*a*c)**0.5))
        else:
            root = x[0] - ((2.0*c)/(b- (b**2 - 4.0*a*c)**0.5))
        print "a = %.5f b = %.5f c = %.5f root = %.5f " % (a,b,c,root)
        print "Current approximation is %.9f" % root
        if abs(evaluate(func,float(root))) > x[0]:
            x = [x[1],x[0],root]
        else:
            x = [x[2],x[0],root]
        x = swap_points(x)
    print_end()

def bisection(func, a, b, max_steps=MaxSteps):
    print_header("Bisection Method", func)
    initial = evaluate(func,float(a))
    for loopCounter in range(max_steps):
        midPoint = a + (b-a)/2.0
        result = evaluate(func,float(midPoint))
        print "Accuracy is within %.9f " % (abs(b-a)/2.0)
        if (result == 0 or ( (abs(b-a)/2.0) > 0)):
            a = midPoint
            initial = result
        else:
            b = midPoint
    print_end()

def regula_falsi(func, a, b, max_steps=MaxSteps, tolerance=Tolerance):
    print_header("regula falsi (false position)",func)
    p = 0.0
    for loopCount in range(max_steps):
        p = b - (evaluate(func,float(b)) * ((a-b)/(evaluate(func,float(a))-evaluate(func,float(b)))))
        print "Current approximation is %.9f" % p
        if (math.copysign(evaluate(func,float(a)),evaluate(func,float(b))) != evaluate(func,float(a))):
            b = p
        else:
            a = p
        if (abs(evaluate(func,float(p))) < tolerance):
            print "Root is %.9f (%d iterations)" % (p,int(loopCount))
            return
    print "Root find cancelled at %.9f" % p
    print_end()

def fixed_point(func, initialApproximation, max_steps=MaxSteps, tolerance=Tolerance):
    print_header("fixed point iteration",func)
    p = initialApproximation
    loopCounter = 1
    for loopCounter in range(max_steps):
        oldP = evaluate(func,float(p))
        print "Current approximation is %.9f" % oldP
        if (abs(p - oldP) < tolerance):
            print "Approximate root is %.9f (found in %d steps)" % (oldP,int(loopCounter))
            return
        p = oldP
    print_end()

def newton_raphson(func, derFunc, initialApproximation, max_steps=MaxSteps, tolerance=Tolerance):
    print_header("newton/raphson",func + " with " + defFunc + " as derivative")
    for loopCounter in range(max_steps):
        p = initialApproximation - (evaluate(func,float(initialApproximation))/evaluate(derFunc,float(initialApproximation)))
        if (abs(p - initialApproximation) < tolerance):
            print "Approximate root is %.9f (found in %i steps)" %(p,loopCounter)
            break
        print "Current approximation %.9f" % initialApproximation
        initialApproximation = p
    print_end()

if __name__ == '__main__':
    try:
        print "in __main__"
        mullers_method(example_f, 0.0, 0.5, 1.0)
    finally:
        print "Fully done."
