Stu_num = [0 for i in range(3)]
total_avg = [0 for i in range(3)]
grade = [0 for i in range(3)]
rank = [1 for i in range(3)]
Middle_Score = 0
Final_Score = 0
report_Score = 0
att_Score = 0
111
for i in range (0,3) :
    Stu_num[i] = input("학번 : ")
    Middle_Score = int(input("중간고사 점수를 입력 : "))
    Final_Score = int(input("기말고사 점수를 입력 : "))
    report_Score = int(input("레포트 점수를 입력 : "))
    att_Score = int(input("출석 점수를 입력 : "))
    total_avg[i] = ((Middle_Score*0.3)+(Final_Score*0.3)+(report_Score*0.2)+(att_Score*0.2))

    if total_avg[i] >= 89.5 :
        grade[i] = 'A'
    elif total_avg[i] >= 79.5 :
        grade[i] = 'B'
    elif total_avg[i] >= 69.5 :
        grade[i] = 'C'
    elif total_avg[i] >= 59.5 :
        grade[i] = 'D'
    else :
        grade[i] = 'F'

for i in range(0,3) :
    for j in range (0,3) :
        if total_avg[i] < total_avg[j] :
            rank[i] += 1

for i in range (0,3) :
    print(f"학번 : {Stu_num[i]} 총점평균 : {total_avg[i]} 학점 : {grade[i]} 등수 : {rank[i]}")