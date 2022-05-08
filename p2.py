students = []
total= []
grade = []
rank = []

student_number = 3
for i in range(student_number) :
    students.append(input('학번:'))
    mid  = int(input('중간고사 점수를 입력하세요. : '))
    last  = int(input('기말고사 점수를 입력하세요. : '))
    report  = int(input('레포트 점수를 입력하세요. : '))
    attend = int(input('출석 점수를 입력하세요. : '))
    total = (mid*0.3) + (last*0.3)+ (report*0.2) + (attend*0.2)
    
    if total >= 89.5:
        grade.append('A')
    elif total >= 79.5:
        grade.append('B')
    elif total >= 69.5:
        grade.append('C')
    elif total >=59.5:
        grade.append('D')    
    else :
        grade.append('F')

for i in range(0, student_number):
    f = student_number
    for j in range(0, student_number):
        if total(i) > total(j):
            f=f-1
        rank.append(f)

for i in range(0, student_number):
    print(f'학번 : {students[i]} , 총점: {total[i]} 학점: {grade[i]},등수 : {rank[i]}')