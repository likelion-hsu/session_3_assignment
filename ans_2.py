score = {}
for i in range(3):
    # 학번, 중간, 기말, 레포트, 출석 점수를 입력 받음
    id = int(input("학번 : "))
    mid = int(input("중간고사 점수를 입력하세요. : "))
    fin = int(input("기말고사 점수를 입력하세요. : "))
    rep = int(input("레포트 점수를 입력하세요. : "))
    att = int(input("출석 점수를 입력하세요. : "))

    # 총점 계산 : 중간 30%, 기말 30%, 레포트 20%, 출석 20%
    total = (mid + fin) / 2 * 0.6 + rep * 0.2 + att * 0.2

    # 학점 계산
    if total >= 89.5:
        hak = 'A'
    elif total >= 79.5:
        hak = 'B'
    elif total >= 69.5:
        hak = 'C'
    elif total >= 59.5:
        hak = 'D'
    else:
        hak = 'F'

    # 학번을 key로 중간, 기말, 레포트, 출석, 총점, 학점 저장
    score[id] = [mid, fin, rep, att, total, hak]

# 석차 계산
for i in score.keys():
    rank = 0
    for j in score.keys():
        # 만약 자신보다 크거나 같은 총점을 가지면
        if score[i][4] <= score[j][4]:
            # 등수를 하나 올림
            rank += 1
        # 추가로 등수 저장
    score[i].append(rank)

# 결과 출력
for i in score.keys():
    print(f'학번 : {i} 총점평균 : {score[i][4]} 학점 : {score[i][5]} 등수 : {score[i][6]}')