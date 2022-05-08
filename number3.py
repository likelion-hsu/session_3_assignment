import random
name=[]
history=[]
word=['침대','룰렛','상자','기사','무사','우산']
last=random.choice(word)
q=int(input('게임에 참가할 인원 수:'))
if q<=1:
    print("경고 다시 해")
    quit()
for i in range(0,q):
    a=input("유저 %d의 닉네임:" %(i+1))
    name.append(a)
print("===========GAME START============")
print(last)
while True:
    r=0
    answer=input(name[r]+":")
    if len(answer)==1:
        print("2글자 이상의 단어만 사용 가능합니다")
        print(name[r]+"탈락")
        name.remove(name[r])
    if  last[-1] != answer[0] :
        print('땡! 틀렸습니다.')
        name.remove(name[r])
        print(last)
    else:
        history.append(answer)
        last = answer 
        r=r+1
print("==========  GAME OVER ===========")
print(f"++++ WINNER : {name[0]} ++++")

