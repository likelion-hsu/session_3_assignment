# 2
list_hakbun = []
list_ave = []
list_rank = [1, 1, 1]
for i in range(0, 3):
    hakbun = int(input('학번 : '))
    list_hakbun.append(hakbun)
    mid = int(input('중간고사 점수를 입력하세요. : '))
    fin = int(input('기말고사 점수를 입력하세요. : '))
    rep = int(input('레포트 점수를 입력하세요. : '))
    att = int(input('출석 점수를 입력하세요. : '))
    sum = mid*0.3 + fin * 0.3 + rep*0.2 + att*0.2
    list_ave.append(sum)

for i in range(0, 3):
    for j in range(0, 3):
        if(list_ave[i] < list_ave[j]):
            list_rank[i] += 1

for i in range(0, 3):
    print('학번 :', list_hakbun[i], "총점평균 :", list_ave[i], sep=" ", end="")
    if(list_ave[i] >= 89.5):
        print(' 학점 : A', list_rank[i], sep=" ")
    elif(list_ave[i] >= 79.5):
        print(' 학점 : B', list_rank[i], sep=" ")
    elif(list_ave[i] >= 69.5):
        print(' 학점 : C', list_rank[i], sep=" ")
    elif(list_ave[i] >= 59.5):
        print(' 학점 : D', list_rank[i], sep=" ")
    else:
        print(' 학점 : F', list_rank[i], sep=" ")
