data = [[],[],[]]
for i in range(3):
    a = input("학번")
    b = int(input("중간고사 점수를 입력하세요. : "))
    c = int(input("기말고사 점수를 입력하세요. : "))
    d = int(input("레포트 점수를 입력하세요. : "))
    e = int(input("출석 점수를 입력하세요. : "))
    data[i].append(a)
    data[i].append(b)
    data[i].append(c)
    data[i].append(d)
    data[i].append(e)
    socore = data[i][1]*0.3+data[i][2]*0.3+data[i][3]*0.2+data[i][4]*0.2
    data[i].append(socore)
    if data[i][5] >= 89.5:
        data[i].append("A")
    elif data[i][5] >= 79.5:
        data[i].append("B")
    elif data[i][5] >= 69.5:
        data[i].append("C")
    elif data[i][5] >= 59.5:
        data[i].append("D")
    else:
        data[i].append("F")
while True:
    if data[0][5] > data[1][5] and data[0][5] > data[2][5]:
        data[0].append(1)
        if data[1][5]>data[2][5]:
            data[1].append(2)
            data[2].append(3)
            break
        else:
            data[1].append(3)
            data[2].append(2)
            break
    elif data[0][5] > data[1][5] or data[0][5] > data[2][5]:
        data[0].append(2)
        if data[1][5]>data[2][5]:
            data[1].append(1)
            data[2].append(3)
            break
        else:
            data[1].append(3)
            data[2].append(1)
            break
    else:
        data[0].append(3)
        if data[1][5]>data[2][5]:
            data[1].append(1)
            data[2].append(2)
            break
        else:
            data[1].append(2)
            data[2].append(1)
            break
for i in range(3):
    print(f"학번  :  {data[i][0]} 총점평균  :  {data[i][5]} 학점  :  {data[i][6]} 등수  :  {data[i][7]}")