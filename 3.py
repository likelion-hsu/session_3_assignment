import random
import sys

number = int(input("게임에 참가할 인원 수 :"))

if number <= 1:
    print("2인 이상 게임 참가 가능 *게임을 다시 시작하세요*")
    sys.exit()

name_list = []
word_list = []
for user in range(1, number+1):
    name_list.append(input(f"유저{user} 닉네임 :"))

i = 0
keyword_list = ["대나무", "무사", "사기", "기사", "사기", "무지개", "개", "기러기", "서산"]

print("========== GAME START ==========")

while len(name_list) != 1:  # 인원수를 체크하는 반복분
    keyword = random.choice(keyword_list)
    word_list.append(keyword)
    print(f"제시어 : [[ {keyword} ]]")

    while True:
        cur_user = name_list[i]

        user_word = input(f"{cur_user} : ")

        if user_word in word_list:
            print("이미 사용된 단어입니다.")
            print(f"** {cur_user} 탈락 **")
            name_list.remove(cur_user)  # 게임인원에서 삭제.
            word_list.clear()  # 게임기록 비우기.
            break

        elif len(user_word) == 1:
            print("2글자 이상의 단어만 사용 가능합니다.")
            print(f"** {cur_user} 탈락 **")
            name_list.remove(cur_user)
            word_list.clear()
            break

        elif word_list[-1][-1] != user_word[0]:
            print("단어가 틀렸습니다.")
            print(f"** {cur_user} 탈락 **")
            name_list.remove(cur_user)
            word_list.clear()
            break

        else:
            word_list.append(user_word)
            i += 1
            if(len(name_list) == i):
                i = 0

print("========= GAME OVER =========")
print(f"+++++ WINNER : {name_list[0]} +++++")
