list= [[0 for j in range(9)] for i in range(3)]
for i in range(3):
    list[i][0] = int(input("학번 : "))
    list[i][1] = int(input("중간고사 점수를 입력하세요. : "))
    list[i][2] = int(input("기말고사 점수를 입력하세요. : "))
    list[i][3] = int(input("레포트 점수를 입력하세요 : "))
    list[i][4] = int(input("출석 점수를 입력하세요 : "))
    list[i][5] = list[i][1]+list[i][2]+list[i][3]+list[i][4]
    list[i][6] = list[i][5]/4
    hak=(int(list[i][6]/10))
    if 9<= hak <=10:
        list[i][7]="A"
    elif hak==8:
        list[i][7]="B"
    elif hak==7:
        list[i][7]="C"
    elif hak==6:
        list[i][7]="D"
    else:
        list[i][7]="F"
        
for i in range(3):
    list[i][8]=1
for i in range(3):
    for j in range(3):
        if list[i][6] < list[j][6]:
            list[i][8]+=1
for i in range(3):
    print("학번 : %s 평균 : %s 학점 : %s 등수 :%s"%(list[i][0],list[i][6],list[i][7],list[i][8]))
   
