import sys
import os
sys.path.append(os.pardir)

from logic_sub import *

def state3(p,q):
    return imp(imp(p,q),imp(imp(p,not q),not p))

def main():
    data_len = 2
    data = gen_data(data_len)

    for i in data:
        print("".join([rev(t) for t in i]))

    for p,q in data:
        print(state3(p,q))




if __name__ == "__main__":
    main()
