# 문제2번 - 3주차 세션 복합 문제
from sys import breakpointhook


student_num = [] # 학번을 넣을 리스트를 선언
total = [] # 총점 평균을 계산해서 넣을 리스트를 선언
grade = [] # 학점을 넣을 리스트를 선언
rank = [] # 순위를 계산해서 넣을 리스트를 선언

count = 0
while True:
    count += 1
    if count > 3: break # 3명까지만 입력을 받습니다.
    student_num.append(input("학번 : "))
    middle_test = int(input("중간고사 점수를 입력하세요. : ")) * 0.3
    final_test = int(input("기말고사 점수를 입력하세요. : ")) * 0.3
    report = int(input("레포트 점수를 입력하세요. : ")) * 0.2
    attend = int(input("출석 점수를 입력하세요. : ")) * 0.2
    total.append(middle_test + final_test + report + attend)
    
    if total[count-1] >= 89.5: grade.append('A')
    elif total[count-1] >= 79.5: grade.append('B')
    elif total[count-1] >= 69.5: grade.append('C')
    elif total[count-1] >= 59.5: grade.append('D')
    else: grade[count-1] = grade.append('F')

## 학생의 총 인원을 최저 등수로 두고, tatal에 있는 점수를 비교하면서 값이 더 큰 경우 1씩 빼서 순위를 결정.
## 동점자가 나왔을 때 등수를 어떻게 처리할까 생각해보다가 해봤습니다...
for i in range(0, len(student_num)):  
    r = len(student_num)
    for j in range(0, len(student_num)): 
        if total[i] > total[j]:
            r = r - 1
    rank.append(r)

# 위에서 입력받고 계산한 정보들을 출력합니다. 
for i in range(0, len(student_num)):
    print(f"학번 : {student_num[i]} 총점평균 : {total[i]} 학점 : {grade[i]} 등수 : {rank[i]}")