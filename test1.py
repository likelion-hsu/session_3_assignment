# 1
import random
list = ['카리나', '윈터', '닝닝', '지젤', '아이린', '조이',
        '예리', '웬디', '미연', '민니', '소연', '우기', '슈화']
for i in range(0, len(list)):
    print(list[i])


# 3
number = int(input('게임에 참가할 인원 수 : '))
if(number <= 1):
    print('               2인 이상 게임 참가 가능',
          '               * 게임을 다시 시작하세요 *', sep='\n')
list_name = []
list_word = ['침대', '대나무', '기사', '사자', '기차', '갈매기', '포도', '햄버거', '커피', '사과']
for i in range(1, number+1):
    name = input('유저 ', i, '의 닉네임 : ')
    list_name.append(name)

print('==========  GAME START  ==========')

print('제시어 : ', random.choice(list_word))
