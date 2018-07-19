from functools import partial

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def imp(a,b):
    return (not a) or b

@Infix
def iff(a,b):
    return imp(a,b) and imp(b,a)

@Infix
def nand(a,b):
    return not (a and b)

def conv(t):
    if t == "0":
        return False
    elif t == "1":
        return True

def rev(t):
    if t == False:
        return "0"
    elif t == True:
        return "1"


def gen_data(data_len):
    data = []
    
    for i in range(2 ** data_len):
        data_tmp = bin(i)[2:]
        if len(data_tmp) < data_len:
            for i in range(data_len - len(data_tmp)):
                data_tmp = "0" + data_tmp

        data_tmp = [conv(x) for x in data_tmp]
        data.append(data_tmp)

    return data
