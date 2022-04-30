import random

Player_num = int(input("게임에 참가할 인원 수 : "))
if Player_num < 2 : 
    print("2인 이상 게임 참가 가능\n* 게임을 다시 시작하세요 *")
    exit()

Player_names = [0 for i in range(Player_num)] # 

Start_word = ["침대", "나무", "사자", "개미", "컴퓨터"]
Game_Data = []

for a in range(0,Player_num) : 
    Player_names[a] = input(f"유저 {a+1}의 닉네임 : ")

print("========   GAME START   ========")
First_word = Start_word[random.randrange(0,5)]
Game_Data.append(First_word)
print(f"제시어 : [[{First_word}]]")
repeat = 0

while True : 

    for a in Player_names :

        if len(Player_names) == 1 :
            print("========   GAME OVER   ========")
            print(f"++++ WINNER : {Player_names[0]} ++++")
            exit()

        Now_word = input(f"{a} : ")
        Front_word = Game_Data[repeat]

        #이전 단어의 마지막 글자와 작성한 단어의 첫 글자가 다를 경우
        if Front_word[-1] != Now_word[0] :
            print("단어가 틀렸습니다.")
            #여기서부턴 다른 if문에도 똑같이 반복사용됨
            print(f"** {a} 탈락 **")
            Player_names.remove(a)
            Game_Data.clear()
            Restart_word = Start_word[random.randrange(0,5)]
            Game_Data.append(Restart_word)
            print(f"제시어 : [[{Restart_word}]]")
            repeat = 0
            break
            #여기까지 반복사용


        # 이미 사용된 단어일 경우
        if  Now_word in Game_Data :
            print("이미 사용한 단어입니다.")
            #여기서부턴 다른 if문에도 똑같이 반복사용됨
            print(f"** {a} 탈락 **")
            Player_names.remove(a)
            Game_Data.clear()
            Restart_word = Start_word[random.randrange(0,5)]
            Game_Data.append(Restart_word)
            print(f"제시어 : [[{Restart_word}]]")
            repeat = 0
            break
            #여기까지 반복사용

        # 단어가 1글자일 경우
        if len(Now_word) == 1 :
            print("두 글자 이상의 단어만 사용 가능합니다.")
            #여기서부턴 다른 if문에도 똑같이 반복사용됨
            print(f"** {a} 탈락 **")
            Player_names.remove(a)
            Game_Data.clear()
            Restart_word = Start_word[random.randrange(0,5)]
            Game_Data.append(Restart_word)
            print(f"제시어 : [[{Restart_word}]]")
            repeat = 0
            break
            #여기까지 반복사용
        
        repeat += 1
        Game_Data.append(Now_word) #if문을 사용하지 않으면 게임데이터 리스트에 단어추가 