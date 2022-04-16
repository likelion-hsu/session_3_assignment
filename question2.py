#문제 2번
students = []    # 0 첫번쨰학생  1 두번째학생 2 세번째학생  학생딕셔너리 담을 리스트 생성

number_student = 3  #학생 
for i in range(number_student):  #학생 한명씩 입력받고 입력받은 값을 리스트에 딕셔너리 형태로 추가
    id = int(input("학번 :"))
    mid = int(input("중간고사 점수를 입력하세요 :"))
    final = int(input("기말고사 점수를 입력하세요 :"))
    report = int(input("레포트 점수를 입력하세요 :"))
    attendance = int(input("출석 점수를 입력하세요 :"))

    #총점 계산 score_average
    score = (mid*0.3)+(final*0.3)+(report*0.2)+(attendance*0.2)

    student = {} #학생 한명 딕셔너리 생성

    student["id"] = id  
    student["mid"] = mid
    student["final"] = final
    student["report"] = report
    student["attendance"] = attendance
    student["score"] = score

    #학점 계산   grades
    if score >= 89.5 :
        student["grades"] = "A"
    elif score >= 79.5 :
        student["grades"] = "B"
    elif score >= 69.5 :
        student["grades"] = "C"
    elif score >= 59.5 :
        student["grades"] = "D"
    else :
        student["grades"] = "F"

    students.append(student) #한명씩 리스트에 넣어줌

# 등수 계산하기  
score_list =[] # score가 높은 순서로 저장할리스트
for student in students :
 #   print(index,student["score"])  # students 리스트에서 인덱스와 score키값을 한번에 가져옴
    score_list.append(student["score"])
    score_list.sort(reverse=True)  # 내림차순

for index,score in enumerate(score_list) :
    for student in students :   # score_list에서 높은 순서대로 student에 score값과 다 비교
        if score == student["score"] :  # score와  student score가 맞다면 딕셔너리에 rank 추가
            student['rank'] = index+1  # for에서 받는 index가 0이니까 +1

# print(score_list)


#출력
for i in range(len(students)):
    print("학번: {} 총점평균: {}  학점: {} 등수: {}".format(students[i]["id"],students[i]["score"],students[i]["grades"], students[i]["rank"] )) 