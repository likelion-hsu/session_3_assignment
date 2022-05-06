from random import randint

import random

word = ["침대","나무","갈매기"] 
user=[]  #유저 이름 저장할 리스트
answer=[] #유저들의 답변을 저장할 리스트

num = int(input("게임에 참가할 인원 수 : "))

#유저 수가 2인이상이 아닐경우 오류메세지
if(num<=1):
    print("\t2인 이상 게임 참가 가능")
    print("\t* 게임을 다시 시작하세요 *")
    exit(1)

#위에서 입력한 인원 수 만큼 닉네임을 입력해준다
for i in range(num):
    user.append(input("유저{}의 닉네임 : ". format(i+1)))
    
print("====== GAME START =====")


i=0 #유저 지정을 위한 인덱스 
k=0 #유저들의 답변을 지정하기 위한 인덱스
n=len(word)-1

#남은 유저가 1명일때 까지 반복
while(len(user)!=1):
    #제시어는 리스트로부터 랜덤으로 출력되지만 다양성을 위해 한번 출력된 제시어는 제거함
    question = word[random.randint(0,n)] 
    print("제시어 : [[ {} ]]".format(question))
    word.remove(question)
    n=n-1
    
    #1명이 탈락할때 까지 반복
    while(True):
        s = input("{} : ".format(user[i])) #유저의 답변을 s에 저장
        
        #답변을 answer리스트에 추가하기전 이미 사용된 단어를 말한 경우 탈락시킴
        if s in answer:
            print("이미 사용한 단어입니다.")
            print("** {} 탈락 ** ".format(user[i]))
            del user[i]   #탈락을 시킨 후 새 게임을 시작해야 하니 모든 변수를 초기값으로 만듬
            answer=[]                 
            k=0
            num=num-1  #탈락 시키면 유저의 수가 1줄어드니 유저 수를 맞춰줘야함(인덱싱 제대로 되기 위해)
            break
        #답변을 리스트에 추가
        answer.append(s) 
        
        #2글지 미만의 단어를 말할 경우
        if(len(answer[k])==1):
            print("2글자 이상의 단어만 사용 가능합니다.")
            print("** {} 탈락 ** ".format(user[i]))
            del user[i]
            answer=[]
            k=0
            num=num-1
            break
        
        #첫답변은 제시어와 비교
        if k==0:
            if(answer[k][0] != question[len(question)-1]):
                print("단어가 틀렸습니다.")
                print("** {} 탈락 ** ".format(user[i]))
                del user[i]
                answer=[]  
                k=0
                num=num-1
                break
        
        #첫답변을 제외한 모든 답변은 이전 유저의 답변과 비교   
        if k!=0:
            if(answer[k][0] != answer[k-1][len(answer[k-1])-1]):
                print("단어가 틀렸습니다.")
                print("** {} 탈락 ** ".format(user[i]))
                del user[i]
                answer=[]
                k=0
                num=num-1
                break
        
        #마지막 유저까지 인덱싱해주고 다시 처음 유저로 인덱스를 돌리기 위함
        if((len(user)==num and i==num-1)): 
            i=-1

        i=i+1
        k=k+1

print("====== GAME OVER =====")
print("++++ WINNER : {} ++++".format(user[0]))