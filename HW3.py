num=int(input("게임에 참여할 인원 수: "))
if num<=1:
    print("2인 이상 게임 참가가능 \n *게임을 다시 시작하세요*")
    exit()
    
user=[] #사용자 리스트 생성
for i in range(num):
    name=input("유저 %d 의 닉네임:" %(i+1))
    user.append(name)
print(name)

history=[] #게임 히스토리
example_str={"침대", "나무","갈매기","거울", "가위"} #집합이라 랜덤으로 나옴(순서X)
    
print("============= GAME START =============")
ex=example_str.pop()
history.append(ex)
print(f"제시어:[[{ex}]]")

while(1<len(user)):  #최종승자 나올때 까지 계속됨.

    for i in user:
        answer=(input(f"{i}:"))  #문자열
        if history[-1][-1]!=answer[0]: #마지막 글자와 첫 글자가 다를 경우(조건1)
            print("단어가 틀렸습니다.")
            print(f"**{i} 탈락**")
            user.remove(i)
            if len(user)==1: continue
            ex=example_str.pop()
            history.append(ex)
            print(f"제시어:[[{ex}]]")
    
        elif answer in history: #사용한 단어일 경우 (조건2)
            print("이미 사용한 단어입니다.")
            print(f"**{i} 탈락**")
            user.remove(i)
            if len(user)==1: continue
            ex=example_str.pop()
            history.append(ex)
            print(f"제시어:[[{ex}]]")
            
        elif len(answer)==1: #단어가 한 글자일 경우
            print("2글자 이상의 단어만 사용 가능합니다.")
            print(f"**{i} 탈락**")
            user.remove(i)
            if len(user)==1: continue
            ex=example_str.pop()
            history.append(ex)
            print(f"제시어:[[{ex}]]")
        else:
            history.append(answer)
        

print("============= GAME OVER =============")
print(f"++++ Winner: {user[0]} ++++")
