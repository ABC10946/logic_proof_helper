from logic_sub import *

def state(a,b):
    return a |iff| b

def state1(a,b):
    (not (a and (not b))) and (not (b and (not a))
