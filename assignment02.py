student_id=[]
avg_score=[]
hakjum = []
rank = []

count =0

while True:
    if(count==3):
        break
    
    student_id.append(input("학번 : "))
    mid_score = int(input("중간고사 점수를 입력하세요 : "))
    fin_score = int(input("기말고사 점수를 입력하세요 : "))
    rep_score = int(input("레포트 점수를 입력하세요 : "))
    att_score = int(input("출석 점수를 입력하세요 : "))
    
    total_score = mid_score*0.3 + fin_score*0.3 + rep_score*0.2 + att_score*0.2
    avg_score.append(total_score)
    
    if total_score >= 89.5:
        hakjum.append('A')
    elif total_score >= 79.5:
        hakjum.append('B')
    elif total_score >= 69.5:
        hakjum.append('C')
    elif total_score >= 59.5:
        hakjum.append('D')
    else:
        hakjum.append('F')
    
    count+=1
    

for i in range(0, len(student_id)):  
    r = 1
    for j in range(0, len(student_id)): #자신의 점수와 다른 학생들의 점수를 비교해서 만약 자기점수가 더 낮다면 rank+1
        if avg_score[i] < avg_score[j]:
            r = r + 1
    rank.append(r)


for i in range(len(student_id)):
    print("학번 : {}  총점평균 : {} 학점 : {} 등수 : {}".format(student_id[i], avg_score[i], hakjum[i], rank[i]))
    

