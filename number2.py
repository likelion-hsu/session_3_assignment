a=[]
total=[]
grade=[]
rank=[]
for i in range(1,4):
    ab=input("학번:")
    a.append(ab)
    score1=int(input("중간고사 점수를 입력하세요"))    
    score2=int(input("기말고사 점수를 입력하세요"))    
    reportscore=int(input("레포트 점수를 입력하세요"))    
    attendance=int(input("출석 점수를 입력하세요"))   
    total.append((score1*0.3)+(score2*0.3)+(reportscore*0.2)+(attendance*0.2))
    if total[i-1]>=89.5:
        grade.append("A")
    elif total[i-1]>=79.5:
        grade.append("B")
    elif total[i-1]>=69.5:
        grade.append("C")
    elif total[i-1]>=59.5:
        grade.append("D")
    else:  grade.append("F")
for i in range(0,len(total)):
    r=1
    for j in range(0,len(total)):
        if total[i]<total[j]:            
            r+=1
            rank.append(r)
            
for i in range (0,len(total)):
    print(f"학번:{a[i]}      총점 평균:{total[i]} 학점:{grade[i]} 등수:{rank[i]}")
    
    