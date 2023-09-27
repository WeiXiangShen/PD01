def transform(card):
    if card == 'A' or card == 'J' or card == 'Q' or card == 'K':
        return 0.5
    else:
        return int(card)

def dataIn():
    data = {}
    for i in range(2):
        name = input()
        data[name] = [transform(input()) for i in range(3)]
        
    return data
def dataProcessAfter(data):
    name = [i for i in data.keys()]
    total = []
    for i in range(2):
        if sum(data[name[i]]) > 10.5:
            total.append(0)
        else:
            total.append(sum(data[name[i]]))

    if total[0] > total[1]:
        print(f"{name[0]} Win")
    elif total[0] < total[1]:
        print(f"{name[1]} Win")
    else:
        print("Tie")

def dataProcessBefore(data):
    name = [i for i in data.keys()]
    total = []
    for i in range(2):
        if sum(data[name[i]]) > 10.5 and i == 0:
            total.append(-1)
        else:
            total.append(sum(data[name[i]]))

    if total[0] > total[1]:
        print(f"{name[0]} Win")
    elif total[0] < total[1]:
        print(f"{name[1]} Win")
    else:
        print("Tie")

def main():
    data = dataIn()
    dataProcessBefore(data)
    dataProcessAfter(data)

main()