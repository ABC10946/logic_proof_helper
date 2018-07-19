from logic_sub import *

def state1(p,q):
    return ((p |imp| q) |imp| p) |imp| p


def main():
    data_len = 2
    data = gen_data(data_len)

    print(data)

    for p,q in data:
        print(state1(p,q))



if __name__ == "__main__":
    main()
