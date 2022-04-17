import random
import sys

n = int(input("게임에 참가할 인원 수 : "))

if n <= 1:

    print("2인 이상 게임 참가 가능\n*게임을 다시 시작하세요*")
    sys.exit()

else:

    uns = []

    for i in range(1, n+1):
        un = input("유저 %s의 닉네임 : " % i)
        uns.append(un)

print("========== GAME START ==========")

gw = []
sw = ['한서대', '멋사', '아기사자']

a = random.choice(sw)

print("제시어 : [[", a, "]]")
gw.append(a)
del(a)

i = 0

while True:

    x = len(uns)

    uw = input("%s :" % uns[i])

    if(uw[0][0]) == (gw[-1][-1]):
        pass
    else:
        print("단어가 틀렸습니다.")
        print(f"** {uns[i]} 탈락 **")
        del uns[i]

    if uw in gw:
        print("이미 사용한 단어입니다.")
        print(f"** {uns[i]} 탈락 **")
        del uns[i]
    else:
        pass

    if len(uw) == 1:
        print("2글자 이상의 단어만 사용 가능합니다.")
        print(f"** {uns[i]} 탈락 **")
        del uns[i]
    else:
        pass

    y = len(uns)

    gw.append(uw)
    del(uw)

    if x > y:
        if y == 1:
            pass
        else:
            del(gw)
            a = random.choice(sw)

            print("제시어 : [[", a, "]]")

            gw = []
            gw.append(a)
            del(a)

            i = i % len(uns)

            del(x)
            del(y)
    else:
        i = (i+1) % len(uns)

    y = len(uns)

    if y == 1:
        print(f"========== GAME OVER ==========\n++++ WINNER : {uns[i]} ++++")
        sys.exit()
