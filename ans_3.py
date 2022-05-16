import random

# 제시어 리스트
words = ['나무', '바나나', '자동차', '갈매기', '토마토', '마우스', '창문', '침대']
# 유저 리스트
names = []
# 게임 차례
turn = 0

# 참가 인원 수 입력받기
n = int(input("게임에 참가할 인원 수 : "))
# 참가 인원이 1명 이하일 경우 경고 메세지 출력 후 프로그램 종료
if n < 2:
    print("""
        2인 이상 게임 참가 가능
        * 게임을 다시 시작하세요 *
    """)
    exit()

# 참가 인원 수 만큼 닉네임 입력 받기
for i in range(n):
    names.append(input(f"유저{i+1}의 닉네임 : "))

# 닉네임 중복 없이 받기 (선택)
# i = 0
# while i < n:
#     name = input(f"유저 {i+1}의 닉네임 : ")
#     if name in names:
#         print("이미 있는 닉네임입니다. 다시 입력해주세요.")
#     else:
#         names.append(name)
#         i += 1

print("==========  GAME START   ==========")
while True:
    # 우승자 제외 모든 유저 탈락시 게임 종료
    if len(names) == 1:
        break

    # 단어 지정 인덱스
    count = 0
    # 사용한 단어 리스트, 한 게임이 끝날 때마다 사용한 단어 리스트 초기화
    wordList = []
    wordList.append(random.choice(words))
    print("제시어 : [[ %s ]]" % wordList[0])

    while True:
        # 끝말잇기 입력 받기, 게임 차례 반복적으로 돌리기
        word = input(f"{names[turn % n]} : ")
        # 사용하지 않은 단어이며, 끝말잇기가 되고, 단어가 한 글자 이상일 경우
        if word not in wordList and word[0] == wordList[count][-1] and len(word) > 1:
            # word를 사용한 단어에 추가
            wordList.append(word)
            # 단어 인덱스 1 증가
            count += 1
            # 게임 차례 1 증가
            turn += 1
        else:
            # 이미 사용한 단어일 경우
            if word in wordList:
                print("이미 사용한 단어입니다.")
            # 단어가 한 글자일 경우
            elif len(word) < 2:
                print("두 글자 이상의 단어만 사용 가능합니다.")
            # 끝말잇기가 되지 않을 경우
            else:
                print("단어가 틀렸습니다.")
            # 해당 유저 탈락 메세지 출력
            print(f"** {names[turn%n]} 탈락 **")
            # 해당 유저 탈락(제거)
            del names[turn % n]
            # 유저 인원 1명 감소
            n -= 1
            break
print("==========  GAME OVER    ==========")
print(f"++++ WINNER : {names[0]} ++++")