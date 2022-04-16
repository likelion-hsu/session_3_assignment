# End-talk 끝말잇기
# 게임시작
# 1. 게임을 참가할 인원 수와 유저 네임을 입력받는다
# (만약 인원이 1 이하일 경우 경고 메세지를 출력하고 프로그램을 종료한다)
# 2. 닉네임 인원 순서대로 게임이 진행된다
# 3. 첫 제시어에는 프로그램에서 랜덤하게 뽑아 사용한다

# 유저가 탈락하는 경우
# 조건1 : 이전 단어의 마지막 글자와 작성한 단어의 첫 글자가 다를 경우
# 조건2 : 이미 사용된 단어일경우
# 조건3 : 단어가 1글자일 경우

# 게임 재개
# 1.새로운판이 시작된다(새로운 제시어를 랜덤으로 뽑아 시작)
# 2. 탈락한 유저 다음 순서부터 시작

import random

# 제시어 리스트
start_list = ["대나무","나무","갈매기","대한민국","한서대학교","컴퓨터","운동","버스","지하철"]


# 참가인원 입력받기
user_names =[]
num_user = int(input("게임에 참가할 인원 수 : "))
if num_user <= 1 :
    print("2인 이상 게임참가 가능");
    print("*게임을 다시 시작하세요*");
    quit()  #  프로그램 종료시키기 

# 유저 이름 입력받기
for i in range(1,num_user+1):
    user_name = input(f"유저{i}의 닉네임 : ")
    user_names.append(user_name)


# 게임시작
print("=========  GAME START  =========")
while len(user_names) != 1 :  # 끝말잇기가 끝나는 조건으로 루프 
    word_list = []  # 게임에 사용될 끝말잇기 리스트
    word = random.choice(start_list)
    print(f"제시어 : [[  {word}  ]]")
    word_list.append(word)
    i = 0 
    while True:
        user_word = input(f"{user_names[i]} :")
        # 조건1 2 3
        if user_word in word_list :
            print("이미 사용한 단어입니다.")
            print(f"** {user_names[i]} 탈락 **") # 탈락 리스트에서 제거
            del user_names[i]
            break
        elif word[-1] != user_word[0] : 
            print("단어가 틀렸습니다.")
            print(f"** {user_names[i]} 탈락 **") # 탈락 리스트에서 제거
            del user_names[i]
            break
        elif len(user_word) == 1 :
            print("2글자 이상의 단어만 사용 가능합니다.")
            print(f"** {user_names[i]} 탈락 **") # 탈락 리스트에서 제거
            del user_names[i]
            break
        else:
            word_list.append(user_word)
            word = user_word
        i= (i+1) % len(user_names) # i를 초기화시켜줌  =
        
            
    
            
print("=========  GAME OVER  =========")
print(f"++++ WINNER : {user_names[0]} ++++")
    

        
