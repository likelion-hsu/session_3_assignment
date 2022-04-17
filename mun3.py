import random

game_num = int(input("게임에 참가할 인원 수 : "))

count = 0
id = []
word_list = []
word = []
last_word = []


if game_num == 1 :
    print("\n")
    print("\t\t2인 이상 게임 참가 가능\n\t\t* 게임을 다시 시작하세요 *")
else :
    for username in range(1,game_num+1) :
        id.append(input(f"유저 {username}의 닉네임 : "))
    print("=========== GAME START ================")
    first_context = ["[침대]","[카메라]","[기차]","[표범]","[차표]",]
    first_choice = random.choice(first_context)
    print(f"제시어 : [{first_choice}]")
    word.append(first_choice)
    word_list.append(word[0])
    last_word = word[0][-1]

    while True:
        for x in range(0,game_num):
            word_list.append(input(id[x]))
            for i in range(1,len(word)):
                if word[i] not in word_list and word[i][0] == last_word:
                    word_list.append(word[i])
                    last_word = word[i][-1]
                else:
                    print("이미 사용된 단어입니다.")


        #history.append(input(f"{id[0]} : "))
        #print(word_list[x+1])

        


