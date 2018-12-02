import sys
import os
sys.path.append(os.pardir)

from logic_sub import *

def state2(p,q,r):
    return imp(p,q) and imp(imp(p,r),imp(p,q and r))

def main():
    data_len = 3
    data = gen_data(data_len)

    for i in data:
        print("".join([rev(t) for t in i]))

    for p,q,r in data:
        print(state2(p,q,r))



if __name__ == "__main__":
    main()
