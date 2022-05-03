import random
firstword = ["침대","합격","해킹","격투","파일","얼굴","멋사","은하수","휴지통"]
user = int(input("게임에 참가할 인원 수 : "))
userdata = []
wordrecode = []
t=0
n=0
if user <= 1:
    print("넌 친구가 없나 보구나 게임할 사람이 1명뿐인걸 보니?")
    quit()
for i in range(1,user+1):
    b = input(f"유저 {i}의 닉네임 : ")
    userdata.append(b)
print("===========  GAME START  ===========")
#len(userdata) == 1
while len(userdata)-1:
    
    if t ==0:
        a = random.randint(0,len(firstword)-1)
        str1 = firstword[a]
        firstword.remove(firstword[a])
        print(f"제시어[{str1}]")
        
    if n==len(userdata):
        n = 0
    str2 = input(f"{userdata[n]} : ")
    if str2[0] == str1[len(str1)-1] and wordrecode.count(str2) == 0 and len(str2) > 1:
        wordrecode.append(str2)
        str1 = str2
        t = 1
        n += 1
    elif len(str2) <= 1:
        print("2글자 이상만 가능")
        print("** {userdata[n]} 탈락 **")
        userdata.remove(userdata[n])
        t = 0
        
            
    elif wordrecode.count(str2) >= 1:
        print("전에 쓴 단어가 나왔어")
        print("** {userdata[n]} 탈락 **")
        userdata.remove(userdata[n])
        t = 0
        
            
    else:
        print("단어가 틀렸습다.")
        print("** {userdata[n]} 탈락 **")
        userdata.remove(userdata[n])
        t = 0
        
print("==========  GAME OVER  ==========")
winnername = userdata[0]
print(f"+++ WINNER : {winnername} +++")
