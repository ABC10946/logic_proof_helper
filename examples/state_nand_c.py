from logic_sub import *

def state_a(a,b,c):
    return a and (b or c)

def state_b(a,b,c):
    return (a |nand| ((b |nand| b) |nand| (c |nand| c))) |nand| (a |nand| ((b |nand| b) |nand| (c |nand| c)))

def state_c(a,b,c):
    return (a |nand| b) |nand| (a |nand| c)

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

    l3 = []
    print("state_c")
    for a,b,c in data:
        r = state_c(a,b,c)
        l3.append(r)
        print(r)

    print("result:"+str(l1 == l2 and l1 == l3))




if __name__ == "__main__":
    main()
