from logic_sub import *

data = gen_data(2)

for p,q in data:
    print(p,q)
    print(p |imp| q)
    
