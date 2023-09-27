def dataInput():
    data = {}
    check = 0
    for i in range(3):
        className = input()
        hour = int(input())

        hourDetail = []
        for j in range(hour):
            tempdata = str(input())
            test = ['1','2','3','4','5','6','7','8','9','a','b','c']
            if int(tempdata[0]) < 1 or int(tempdata[0]) > 5 or tempdata[1] not in test:
                check = -1
            hourDetail.append(tempdata)
        data[className] = hourDetail
            
    if check == -1:
        return -1
    else:
        return data

def dataProcess(data):
    className = [i for i in data.keys()]
    check = 0
    for i in data[className[0]] :
        if i in data[className[1]]:
            print(f"{className[0]},{className[1]},{i}")
            check = 1
        if i in data[className[2]]:
            print(f"{className[0]},{className[2]},{i}")
            check = 1

    for i in data[className[1]] :
        if i in data[className[2]]:
            print(f"{className[1]},{className[2]},{i}")
            check = 1

    if check == 0:
        print("correct")
    

  
        

def main():
    data = dataInput()
    if data == -1:
        print(-1)
        return 0
    dataProcess(data)

main()