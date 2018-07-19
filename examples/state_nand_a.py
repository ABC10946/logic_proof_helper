from logic_sub import *

def state_a(a,b):
    return (not a) |imp| (not b)

def state_b(a,b):
    return ((a |nand| b) |nand| b)

def main():
    data_len = 2
    data = gen_data(data_len)

    print("state_a")
    l1 = []
    for a,b in data:
        r = state_a(a,b)
        l1.append(r)
        print(r)

    print("state_b")
    l2 = []
    for a,b in data:
        r = state_b(a,b)
        l2.append(r)
        print(r)

    print("result:"+str(l1 == l2))




if __name__ == "__main__":
    main()
