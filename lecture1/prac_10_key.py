

human = {3:"김영희", 100:"김철수"}
print(human[3])
print(human.get(100))

#print(human[5])  #오류를 발생, 프로그램 종료
print(human.get(5)) #일단은 시도, 없으면 none
print(human.get(5,"없어용"))


print(3 in human) #3이라는 키가 있나?
print(5 in human) #5 있냐?

#키는 숫자가 아니여도 된다
human2 ={"A":"로빈", "B":"존"}
print(human2["A"])
print(human2.get("B"))

#추가
human2["C"] ="빅터"
#수정
human2["A"]="로빈손"

print(human2)

#삭제
del human2["A"]
print(human2)

print(human2.keys())
print(human2.values())

print(human2.items())

#전체 삭제
human2.clear()
print(human2)