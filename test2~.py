# 배열준비
students = []
total = []
hak = []
rank = []

# 해당항에  각각의 배열에 추가
num = 3
for i in range(num):
    students.append(input("학번 : "))
    b = int(input("중간고사 점수를 입력하세요. : "))*0.3
    c = int(input("기말고사 점수를 입력하세요. : "))*0.3
    d = int(input("레포트 점수를 입력하세요 : "))*0.2
    e = int(input("출석 점수를 입력하세요. : "))*0.2
    total.append(b+c+d+e)

    if total[i] >= 89.5:
        hak.append("A")
    elif total[i] >= 79.5:
        hak.append("B")
    elif total[i] >= 69.5:
        hak.append("C")
    elif total[i] >= 59.5:
        hak.append("D")
    else:
        hak.append("F")


for i in range(0, num):
    r = num
    for j in range(0, num):
        if total[i] > total[j]:
            r = r - 1
    rank.append(r)


for i in range(0, num):
    print(f'학번: {students[i]}  총점 : {total[i]} 학점 : {hak[i]}, 등수 : {rank[i]} ')
