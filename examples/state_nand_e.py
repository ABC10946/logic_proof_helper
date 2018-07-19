from logic_sub import *

def state_a(a,b,c):
    return (not a) |imp| ((not b) |imp| c)

def state_b(a,b,c):
    return (a |nand| a) |nand| ((((b |nand| b) |nand| (c |nand| c)) |nand| ((b |nand| b) |nand| (c |nand| c))))

def main():
    data_len = 3
    data = gen_data(data_len)

    l1 = []
    print("state_a")
    for a,b,c in data:
        r = state_a(a,b,c)
        l1.append(r)
        print(r)

    l2 = []
    print("state_b")
    for a,b,c in data:
        r = state_b(a,b,c)
        l2.append(r)
        print(r)

    print("result:"+str(l1 == l2))




if __name__ == "__main__":
    main()
