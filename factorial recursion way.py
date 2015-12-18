###factorial recursion way###
# recursion always returns
# end condition is the first thing your need
# good way is to use that first condition in a 'if' loop
# http://www.codeskulptor.org/#user40_nM5B9iTTXA_1.py
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print factorial(16)
