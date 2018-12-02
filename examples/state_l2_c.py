import sys
import os
sys.path.append(os.pardir)
from logic_sub import *

def state(p,q,r):
    return (p |imp| (q |imp| r)) |iff| ((p and q) |imp| r)

def main():
    data_len = 3
    data = gen_data(data_len)

    for i in data:
        print("".join([rev(t) for t in i]))

    for p,q,r in data:
        print(state(p,q,r))


if __name__ == "__main__":
    main()
