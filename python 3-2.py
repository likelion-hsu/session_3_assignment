classof = []
score = []
hak = []
rank = []

person = 0

while True:
  
  person += 1
  
  if person > 3: break
  
  classof.append(input("학번 : "))
  mid = int(input("중간고사 점수를 입력하세요. : "))
  final = int(input("기말고사 점수를 입력하세요. : "))
  report = int(input("레포트 점수를 입력하세요. : "))
  attend = int(input("출석 점수를 입력하세요. : "))

  tempscore = (mid * 0.3) + (final * 0.3) + (report * 0.2) + (attend * 0.2)
  score.append(tempscore)
  
  if tempscore >= 89.5:
    hak.append('A')
  elif tempscore >= 79.5:
    hak.append('B')
  elif tempscore >= 69.5:
    hak.append('C')
  elif tempscore >= 59.5:
    hak.append('D')
  else: 
    hak.append('F')

for i in range(0, person):
  r = person
  for j in range(0, person):
    if score[i-1] > score[j-1]:
      r = r - 1
rank.append(r)

for i in range(0, person):
  print(f"학번 : {classof[i]} 총점평균 : {score[i]} 학점 : {hak[i]} 등수 : {rank[i]}")
