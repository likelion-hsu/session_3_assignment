import random
list_word = ['침대', '대나무', '기사', '사자', '기차', '갈매기', '포도', '햄버거', '커피', '사과']
number = int(input('게임에 참가할 인원 수 : '))
if(number <= 1):
    print('               2인 이상 게임 참가 가능',
          '               * 게임을 다시 시작하세요 *', sep='\n')
list_name = []
data = []
for i in range(1, int(number+1)):
    list_name.append(input(f"유저{i}의 닉네임 :  "))

print('==========  GAME START  ==========')
first_word = random.choice(list_word)
print('제시어 : ', first_word)
count = 0
while len(list_name) > 1:
    user = len(list_name)
    i = list_name[count % user]
    word = input(f"{i} : ")
    if 1 == len(word):
        print('2글자 이상의 단어만 사용 가능합니다.')
        print(f"** {i} 탈락 **")
        indexx = list_name.index(i)
        list_name.remove(i)
    elif first_word[-1] != word[0]:
        print('단어가 틀렸습니다.')
        print(f"** {i} 탈락 **")
        indexx = list_name.index(i)
        list_name.remove(i)
    elif word in data or word == first_word:
        print('이미 사용한 단어입니다.')
        print(f"** {i} 탈락 **")
        indexx = list_name.index(i)
        list_name.remove(i)

    if len(list_name) == user-1:
        data = []
        count = indexx
        first_word = random.choice(list_word)
        print('제시어 : ', first_word)
    else:
        count += 1
        data.append(word)
        first_word = word
print('==========  GAME OVER ===========')
print('++++ WINNER : ', list_name[0], ' ++++')
