student_number =[]
avg=[]
grade=[]
rank = []
#해당항에 각 배열에 추가
num=3
for i in range(num):
    student_number.append(input("학번 : "))
    middle= int(input("중간고사 점수를 입력하세요. :"))*0.3
    last=int(input("기말고사 점수를 입력하세요. :"))*0.3
    report=int (input("레포트 점수를 입력하세요 . :"))*0.2
    check=int (input("출석 점수를 입력하세요. :"))*0.2
    avg.append(middle+last+report+check)

    if avg[i]>=89.5:
        grade.append("A")
    elif avg[i]>=79.5:
        grade.append("B")
    elif avg[i]>=69.5:
        grade.append("C")
    elif avg[i]>=59.5:
        grade.append("D")
    else:
        grade.append("F")

for i in range(0, num):
    a=num
    for j in range(0, num):
        if avg[i]>avg[j]:
            a=a-1
        rank.append(a)

for i in range(0,num):
    print(f'학번: {student_number[i]} 총점 : {avg[i]} 학점 : {grade[i]}, 등수 : {rank[i]}')    
