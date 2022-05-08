#1번
# data = [['카리나','윈터','닝닝','지젤'],['아이린','조이','슬기','예리'],['미연','미니','소연','우기','슈화']]
# for girl in data:
#     for member in girl:
#         print(member)

#2번 최초 시도 실패 코드

# list = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# for i in range(0,3):
#     hak = (int)(input("학번 : "))
#     jg = (int)(input("중간고사 점수를 입력하세요. :"))
#     gg = (int)(input("기말고사 점수를 입력하세요. :"))
#     lp = (int)(input("레포트 점수를 입력하세요. :"))
#     cs = (int)(input("출석 점수를 입력하세요. :"))
#     sum = ((jg*0.3) + (gg*0.3) + (lp*0.2) + (cs*0.2))
#     if sum>=89.5:
#             total = 'A'
#     elif sum>=79.5:
#             total = 'B'
#     elif sum>=69.5:
#             total = 'C'
#     elif sum>=59.5:
#             total = 'D'
#     else:
#             total='F'
#     if i==0:
#         list[0][0]=hak
#         list[0][1]=sum
#         list[0][2]=total
#     elif i==1:
#         list[1][0]=hak
#         list[1][1]=sum
#         list[1][2]=total
#     elif i==1:
#         list[2][0]=hak
#         list[2][1]=sum
#         list[2][2]=total

#     last=[list[0][2],list[1][2],list[2][2]]
#     last.sort #list정렬로 등수 정하기
    
# if last[0]==list[0][2]: #list의 첫번째가 1등일때
#     list[0][3]="1등"
#     if last[1]==list[1][2]: #list의 두번째가 2등일때,list의 세번째가 3등
#         list[1][3]="2등"
#         list[2][3]="3등"
#     else:
#         list[2][3]="2등"
#         list[1][3]="3등"
    
# elif last[0]==last[1][2]: #list의 두번째가 1등일때
#     list[1][2],"1등"
#     if last[1]==list[0][2]: #list의 첫째가 2등일때,list의 세번째가 3등
#         list[0][3]="2등"
#         list[2][3]="3등"
#     else: #list의 셋째가 2등일때, list의 첫번째가 3등
#         list[2][3]="2등"
#         list[0][3]="3등"
    
# else: #list의 세번째가 1등일때
#     list[2][3]="1등"
#     if last[1]==list[0][2]: #list의 첫째가 2등일때,list의 두번째가 3등
#         list[0][3]="2등"
#         list[1][3]="3등"
#     else: #list의 두번째가 2등일때, list의 첫번째가 3등
#         list[1][3]="2등"
#         list[0][3]="3등"
        
# for i in range(3):
#     print("학번 : ")
#     print(list[i][0])
#     print(" 총점평균 : ")
#     print(list[i][1])
#     print(" 학점 :")
#     print(list[i][2])
#     print(" 등수 : ")
#     print(list[i][3])
#     print("\n")
        
    # if i == 0:
    #     hj0="학번 : %d 총점평균 : %d 학점 : %s" %(hak,sum,total)
    # elif i==1:
    #     hj1="학번 : %d 총점평균 : %d 학점 : %s" %(hak,sum,total)
    # elif i==2:
    #     hj2="학번 : %d 총점평균 : %d 학점 : %s" %(hak,sum,total)


##############################2번##############################
dic = {} #데이터를 넣을 dictionary 생성
dic = dict() 
for i in range(0,3): #3번 반복
    hak = (int)(input("학번 : "))
    jg = (int)(input("중간고사 점수를 입력하세요. :"))
    gg = (int)(input("기말고사 점수를 입력하세요. :"))
    lp = (int)(input("레포트 점수를 입력하세요. :"))
    cs = (int)(input("출석 점수를 입력하세요. :"))
    sum = ((jg*0.3) + (gg*0.3) + (lp*0.2) + (cs*0.2))
    if sum>=89.5:
            total = 'A'
    elif sum>=79.5:
            total = 'B'
    elif sum>=69.5:
            total = 'C'
    elif sum>=59.5:
            total = 'D'
    else:
            total='F'
    if i==0:
        dic['hak1']=hak
        dic['sum1']=sum
        dic['total1']=total
    elif i==1:
        dic['hak2']=hak
        dic['sum2']=sum
        dic['total2']=total
    elif i==2:
        dic['hak3']=hak
        dic['sum3']=sum
        dic['total3']=total
        
if (dic['sum1'] > dic['sum2'] and dic['sum1'] > dic['sum3']): # 1번째 > 2번째 and 1번째 > 3번째
    dic['num1']='1등' #1등 (1번째)
    if (dic['sum2'] > dic['sum3']): #(2번째 > 3번째) => 1번째 2번째 3번째      
        dic['num2']='2등'
        dic['num3']='3등'
    elif(dic['sum3'] > dic['sum2']): #(3번째 > 2번째) => 1번째 3번째 2번쨰     
        dic['num3']='2등'
        dic['num2']='3등'

elif (dic['sum2'] > dic['sum1'] and dic['sum2'] > dic['sum3']): # 2번째 > 1번째 and 2번째 > 3번째
    dic['num2']='1등' #1등 (2번째)
    if(dic['sum1'] > dic['sum3']): #(1번째 > 3번째) => 2번째 1번째 3번째
        dic['num1']='2등'
        dic['num3']='3등'
    elif(dic['sum3'] > dic['sum1']): #(3번째 > 1번째) => 2번째 3번째 1번째
        dic['num3']='2등'
        dic['num1']='3등'

elif (dic['sum3'] > dic['sum1'] and dic['sum3'] > dic['sum2']): # 3번째 > 1번째 and 3번째 > 2번째
    dic['num3']='1등' #1등 (3번째)
    if(dic['sum1'] > dic['sum2']): #(1번째 > 2번째) => 3번째 1번째 2번째
        dic['num1']='2등'
        dic['num2']='3등'
    elif(dic['sum3'] > dic['sum1']): #(2번째 > 1번째) => 3번째 2번째 1번째
        dic['num2']='2등'
        dic['num1']='3등'
   
print("학번 :", dic['hak1'],"총점평균 : ",dic['sum1'], "학점 : ",dic['total1'], "등수 : ",dic['num1'])
print("학번 :", dic['hak2'],"총점평균 : ",dic['sum2'], "학점 : ",dic['total2'], "등수 : ",dic['num2'])
print("학번 :", dic['hak3'],"총점평균 : ",dic['sum3'], "학점 : ",dic['total3'], "등수 : ",dic['num3'])

