student_num = [] # 학번 리스트 선언
total = [] # 총점 평균 리스트 선언
grade = [] # 학점을 넣을 리스트 선언
rank = [] # 순위를 계산해서 넣을 리스트 선언

count = 0
while True:
    count += 1
    if count > 3: break # 3명까지만 입력을 받습니다.
    #append : 리스트에 맨 마지막에 요소를 추가하는 함수
    #반복문을 돌리다 보면 이 추가하는 함수가 없으면 리스트가 초기화된다.
    student_num.append(input("학번 : "))
    middle_test = int(input("중간고사 점수를 입력하세요. : "))
    final_test = int(input("기말고사 점수를 입력하세요. : "))
    report = int(input("레포트 점수를 입력하세요. : "))
    attend = int(input("출석 점수를 입력하세요. : "))
    total.append((middle_test * 0.3) + (final_test * 0.3) + (report * 0.2) + (attend * 0.2))
    
    #count가 이미 1부터 시작했으므로 리스트에 첫번째요소는 0번째이므로
    #total[1-1=0] >> total[2-1=1] >> 순으로 채워진다.
    if total[count-1] >= 89.5: grade.append('A')
    elif total[count-1] >= 79.5: grade.append('B')
    elif total[count-1] >= 69.5: grade.append('C')
    elif total[count-1] >= 59.5: grade.append('D')
    else: grade[count-1] = grade.append('F')

#리스트 중간 점검
#print(student_num)
#print(total)
#print(grade)

rank = [1,1,1]
for i in range(0, len(student_num)):  
    rank[i] =1
    for j in range(0, len(student_num)): 
        if total[i] < total[j]:
            rank[i] = rank[i]+1

#등수 리스트 점검
#print(rank)

for i in range(0, len(student_num)):
    print("학번 : "+student_num[i])+print("총점 평균 :" + total[i])
    # + " 총점평균 : " + total[i] + " 학점 : " + grade[i] + " 등수 : " + rank[i])
