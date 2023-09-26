def planA(data):
    total = 0
    if (data[5] - 1) > 0:
        total = data[0] * 0.08 + data[1] * 0.139 + data[2] * 0.135 + data[3] * 1.128 + data[4] * 1.483 + (data[5] - 1) * 250 
    else:
        total = data[0] * 0.08 + data[1] * 0.139 + data[2] * 0.135 + data[3] * 1.128 + data[4] * 1.483 
    
    if total < 183:
        return 183
    else:
        return total
def planB(data):
    total = 0
    if (data[5] - 3) > 0:
        total = data[0] * 0.07 + data[1] * 0.130 + data[2] * 0.121 + data[3] * 1.128 + data[4] * 1.483 + (data[5] - 3) * 200 
    else:
        total = data[0] * 0.07 + data[1] * 0.130 + data[2] * 0.121 + data[3] * 1.128 + data[4] * 1.483 
    
    if total < 383:
        return 383
    else:
        return total
def planC(data):
    total = 0
    if (data[5] - 5) > 0:
        total = data[0] * 0.06 + data[1] * 0.108 + data[2] * 0.101 + data[3] * 1.128 + data[4] * 1.483 + (data[5] - 5) * 150 
    else:
        total = data[0] * 0.06 + data[1] * 0.108 + data[2] * 0.101 + data[3] * 1.128 + data[4] * 1.483 
    
    if total < 983:
        return 983
    else:
        return total
def planD(data):
    total = data[0] * 0.05 + data[1] * 0.1 + data[2] * 0.090 + data[3] * 1.128 + data[4] * 1.483 
    
    if total < 1283:
        return 1283
    else:
        return total
    
def main():
    data = [int(input()) for i in range(6)]
    cost = [planA(data), planB(data), planC(data), planD(data)]
    plan = [183,383,983,1283]
    print(int(min(cost)))
    print(plan[cost.index(min(cost))])

main()