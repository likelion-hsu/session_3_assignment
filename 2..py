number = []
total_score = []
grade = []
rank = []

for x in range(3):
    number.append(int(input("학번을 입력 해주세요 :")))
    midterm_exam = float(input("중간고사 점수를 입력하세요 :"))
    final_exam = float(input("기말고사 점수를 입력하세요 :"))
    report_score = float(input("출석 점수를 입력하세요 :"))
    attendance_score = float(input("레포트 점수를 입력하세요 :"))
    total_score.append(midterm_exam*0.3+final_exam
                       * 0.3+report_score*0.2+attendance_score*0.2)


for x in total_score:
    if x > 89.5:
        grade.append("A")
    elif x > 75.9:
        grade.append("B")
    elif x > 65.9:
        grade.append("C")
    elif x > 59.5:
        grade.append("D")
    else:
        grade.append("F")

temp = list(reversed(sorted(total_score)))
for score in total_score:
    rank.append(temp.index(score)+1)

for i in range(3):
    print(f'학번:{number[i]} 총점:{total_score[i]} 학점:{grade[i]} 등수:{rank[i]}')
