stu={} #학생 딕셔너리

for i in range(3):
    sub=[] #리스트
    num=input("학번:")
    sub.append(int(input("중간고사 점수를 입력하세요.:")))
    sub.append(int(input("기말고사 점수를 입력하세요.:")))
    sub.append(int(input("레포트 점수를 입력하세요.:")))
    sub.append(int(input("출석 점수를 입력하세요.:")))
    total=(sub[0]*0.3)+(sub[1]*0.3)+(sub[2]*0.2)+(sub[3]*0.2) #총점
    sub.append(total) 
    while(total):
        if total>=89.5:
            sub.append('A')
            break
        elif total>=79.5:
            sub.append('B')
            break
        elif total>=69.5:
            sub.append('C')
            break
        elif total>=59.5:
            sub.append('D')
            break
        else:
            sub.append('F')
            break
    stu[num]=sub

rank=[] #sort()사용을 위한 리스트
for i in stu.keys():
    rank.append(stu[i][4])
rank.sort()

b={} #등수 저장 딕셔너리
j=len(rank)
for i in rank:
    b[i]=j
    j-=1

for i in stu.keys(): #stu{키값(학번):총점} <=>b{총점: 등수} 연결
    for k in b.keys():
        if stu[i][4]==k:
            temp=b.get(k)
            stu[i].append(temp)
            
for i in stu.keys():
    print(f"학번:{i} 총점평균:{stu[i][4]} 학점: {stu[i][5]} 등수: {stu[i][6]}")

