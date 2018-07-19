from logic_sub import *

def state_a(a,b):
    return a and (not b)

def state_b(a,b):
    return (a |nand| (b |nand| b)) |nand| (a |nand| (b |nand| b))

def main():
    data_len = 2
    data = gen_data(data_len)

    l1 = []
    print("state_a")
    for a,b in data:
        r = state_a(a,b)
        l1.append(r)
        print(r)

    l2 = []
    print("state_b")
    for a,b in data:
        r = state_b(a,b)
        l2.append(r)
        print(r)

    print("result:"+str(l1 == l2))




if __name__ == "__main__":
    main()
