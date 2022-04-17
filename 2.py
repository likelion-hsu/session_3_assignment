print("학번 : 1111")
am = int(input("중간고사 점수를 입력하세요. : "))
af = int(input("기말고사 점수를 입력하세요. : "))
ar = int(input("레포트 점수를 입력하세요. : "))
aa = int(input("출석 점수를 입력하세요. : "))

print("학번 : 2222")
bm = int(input("중간고사 점수를 입력하세요. : "))
bf = int(input("기말고사 점수를 입력하세요. : "))
br = int(input("레포트 점수를 입력하세요. : "))
ba = int(input("출석 점수를 입력하세요. : "))

print("학번 : 3333")
cm = int(input("중간고사 점수를 입력하세요. : "))
cf = int(input("기말고사 점수를 입력하세요. : "))
cr = int(input("레포트 점수를 입력하세요. : "))
ca = int(input("출석 점수를 입력하세요. : "))

at = am*0.3 + af*0.3 + ar*0.2 + aa*0.2
bt = bm*0.3 + bf*0.3 + br*0.2 + ba*0.2
ct = cm*0.3 + cf*0.3 + cr*0.2 + ca*0.2

if at >= 89.5:
    ag = 'A'
elif at >= 79.5 and at < 89.5:
    ag = 'B'
elif at >= 69.5 and at < 79.5:
    ag = 'C'
elif at >= 59.5 and at < 69.5:
    ag = 'D'
else:
    ag = 'F'

if bt >= 89.5:
    bg = 'A'
elif bt >= 79.5 and bt < 89.5:
    bg = 'B'
elif bt >= 69.5 and bt < 79.5:
    bg = 'C'
elif bt >= 59.5 and bt < 69.5:
    bg = 'D'
else:
    bg = 'F'

if ct >= 89.5:
    cg = 'A'
elif ct >= 79.5 and ct < 89.5:
    cg = 'B'
elif ct >= 69.5 and ct < 79.5:
    cg = 'C'
elif ct >= 59.5 and ct < 69.5:
    cg = 'D'
else:
    cg = 'F'

if at > bt and at > ct:
    a = 1
    if bt > ct:
        b = 2
        c = 3
    else:
        b = 3
        c = 2
elif bt > at and bt > ct:
    b = 1
    if at > ct:
        a = 2
        c = 3
    else:
        a = 3
        c = 2
else:
    c = 1
    if at > bt:
        a = 2
        c = 3
    else:
        a = 3
        c = 2

print("학번 : 1111 총점평균 : ", at, "학점 : ", ag, "등수 : ", a)
print("학번 : 1111 총점평균 : ", bt, "학점 : ", bg, "등수 : ", b)
print("학번 : 1111 총점평균 : ", ct, "학점 : ", cg, "등수 : ", c)
