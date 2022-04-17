hak = int(input("학번 : "))
hak1 = int(input("중간고사 점수를 입력하세요. : "))
hak2 = int(input("기말고사 점수를 입력하세요. : "))
hak3 = int(input("레포트 점수를 입력하세요. : "))
hak4 = int(input("출석 점수를 입력하세요. : "))
tot_1 = hak1*0.3 + hak2*0.3 + hak3*0.2 + hak4*0.2

gak = int(input("학번 : "))
gak1 = int(input("중간고사 점수를 입력하세요. : "))
gak2 = int(input("기말고사 점수를 입력하세요. : "))
gak3 = int(input("레포트 점수를 입력하세요. : "))
gak4 = int(input("출석 점수를 입력하세요. : "))
tot_2 = gak1*0.3 + gak2*0.3 + gak3*0.2 + gak4*0.2

jak = int(input("학번 : "))
jak1 = int(input("중간고사 점수를 입력하세요. : "))
jak2 = int(input("기말고사 점수를 입력하세요. : "))
jak3 = int(input("레포트 점수를 입력하세요. : "))
jak4 = int(input("출석 점수를 입력하세요. : "))
tot_3 = jak1*0.3 + jak2*0.3 + jak3*0.2 + jak4*0.2

if tot_1 > 89.5 :
    score_1 = 'A'
elif tot_1 > 79.5 :
    score_1 = 'B'
elif tot_1 > 69.5 :
    score_1 = 'C'
elif tot_1 > 59.5 :
    score_1 = 'D'
else :
    score_1 = 'F'

if tot_2 > 89.5 :
    sco_1 = 'A'
elif tot_2 > 79.5 :
    sco_1 = 'B'
elif tot_2 > 69.5 :
    sco_1 = 'C'
elif tot_2 > 59.5 :
    sco_1 = 'D'
else :
    sco_1 = 'F'

if tot_3 > 89.5 :
    scor_1 = 'A'
elif tot_3 > 79.5 :
    scor_1 = 'B'
elif tot_3 > 69.5 :
    scor_1 = 'C'
elif tot_3 > 59.5 :
    scor_1 = 'D'
else :
    scor_1 = 'F'

if tot_1 > tot_2 and tot_1 > tot_3 :
    asu = 1
    if tot_2 > tot_3 :
        bsu = 2
        csu = 3
    else :
        bsu = 3
        csu = 2
    print(f"학번 : {hak} 총점평균 : {tot_1} 학점 : {score_1} 등수 : {asu}")
    print(f"학번 : {gak} 총점평균 : {tot_2} 학점 : {sco_1} 등수 : {bsu}")
    print(f"학번 : {jak} 총점평균 : {tot_3} 학점 : {scor_1} 등수 : {csu}")
elif tot_2 > tot_3 and tot_2 > tot_1 :
    bsu = 1
    if tot_1 > tot_3 :
        asu = 2
        csu = 3
    else :
        absu = 3
        csu = 2
    print(f"학번 : {hak} 총점평균 : {tot_1} 학점 : {score_1} 등수 : {asu} ")
    print(f"학번 : {gak} 총점평균 : {tot_2} 학점 : {sco_1} 등수 : {bsu}" )
    print(f"학번 : {jak} 총점평균 : {tot_3} 학점 : {scor_1} 등수 : {csu}" )
else :
    csu = 1
    if tot_1 > tot_2 :
        asu = 2
        bsu = 3
    else :
        absu = 3
        bsu = 2
    print(f"학번 : {hak} 총점평균 : {tot_1} 학점 : {score_1} 등수 : {asu}")
    print(f"학번 : {gak} 총점평균 : {tot_2} 학점 : {sco_1} 등수 : {bsu}")
    print(f"학번 : {jak} 총점평균 : {tot_3} 학점 : {scor_1} 등수 : {csu}")