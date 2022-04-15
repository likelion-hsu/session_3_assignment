# 문제 3번 - 끝말잇기 (End - Talk)
import random

count = 0
user = []
word_list = ['침대', '나무', '갈매기']
word_data = []

number = int(input("게임에 참가할 인원 수 : ")) # 게임에 참가할 인원 수를 입력 받는다.
if number <= 1: # 게임 인원이 1명 이하일 경우에 게임이 진행되지 않고, 종료된다.
    print("""
            2인 이상 게임 참가 가능
            * 게임을 다시 시작하세요 *""")
    exit()

for i in range(1, number + 1): # 유저의 이름을 입력 받아서 리스트에 저장한다.
    user.append(input(f"유저{i}의 닉네임 :  "))

print("==========  GAME START ===========")

before_word = random.choice(word_list) # 첫 제시어는 프로그램에서 랜덤으로 뽑는다.
print(f"제시어 : [[ {before_word} ]]")

while True:
    user_num = len(user)
    i = user[count % user_num]
    input_word = input(f"{i} : ")
    
    if len(input_word) == 1: ## 탈락 조건 3 : 단어가 1글자일 경우
        print("2글자 이상의 단어만 사용 가능합니다.")
        print(f"** {i} 탈락 **")
        flag = user.index(i); user.remove(i)
    elif before_word[-1] != input_word[0]: # 탈락 조건 1 : 이전 단어의 마지막 글자와 작성한 단어의 첫 글자가 다를 경우
        print("단어가 틀렸습니다.")
        print(f"** {i} 탈락 **")
        flag = user.index(i); user.remove(i) # 탈락한 사람을 user 리스트에서 없앤다.
    elif input_word in word_data or input_word == before_word: # 탈락 조건 2 : 이미 사용된 단어일 경우
        print("이미 사용한 단어입니다.")
        print(f"** {i} 탈락 **")
        flag = user.index(i); user.remove(i)
    
    
    if len(user) == user_num-1 and len(user) != 1: # 게임을 제게하기 위한 조건 (새로운 탈락자 발생)
        word_data = [] # 새로운 게임이 열리기 때문에 입력받은 단어를 저장하는 리스트를 초기화
        count = flag # 탈락한 유저 다음 순서부터 시작하기 위한 조건 : 탈락한 사람의 index를 저장해놨던 flag를 count 변수에 넣는다.
        before_word = random.choice(word_list) # 새로운 판이 시작된다. (새로운 제시어를 랜덤으로 뽑아 시작)
        print(f"제시어 : [[ {before_word} ]]")
    elif len(user) == 1: # 모두 탈락하고 user 리스트에 혼자 남게되면 게임 종료
        print("==========  GAME OVER ===========")
        print(f"++++ WINNER : {user[0]} ++++")
        break
    else: # 아무도 탈락하지 않고 계속 진행될 경우에는 count에 1씩 더해서 다음 순서로 이동
        count += 1
        word_data.append(input_word) # 입력 받은 단어를 word_data 리스트에 넣는다. 이미 사용한 단어를 찾기 위함
        before_word = input_word # 이전 단어의 끝 자리와 비교하기 위해서  입력 받은 단어를 before_word 변수에 넣는다.