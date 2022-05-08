id = []
avg = []
grade = []
num = []

for i in range(3):
    id.append(input("학번 : "))
    mid = float(input("중간고사 점수를 입력하세요. : "))
    final = float(input("기말고사 점수를 입력하세요. : "))
    report = float(input("레포트 점수를 입력하세요. : "))
    att = float(input("출석 점수를 입력하세요. : "))
    avg.append(mid*0.3 + final*0.3 + report*0.2 + att*0.2)

    if avg[i] >= 89.5:
        grade.append("A")
    elif avg[i] >= 79.5:
        grade.append("B")
    elif avg[i] >= 69.5:
        grade.append("C")
    elif avg[i] >= 59.5:
        grade.append("D")
    else:
        grade.append("F")

for i in range(3):
    x = 3
    for j in range(3):
        if avg[i] > avg[j]:
            x -= 1
    num.append(x)

for i in range(3):
    print(f"학번 : {id[i]} 총점 : {avg[i]} 학점 : {grade[i]}, 등수 : {num[i]}")
