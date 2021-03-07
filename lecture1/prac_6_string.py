sentence ="ABC abc"

print(sentence.lower())  #소문자 출력
print(sentence.upper())  #대문자 출력
print(sentence[0].isupper()) #[n]번째 글자가 대문자입니까?
print(len(sentence))    #문장 길이 (띄어쓰기 포함)

print(sentence.replace("abc","DEF")) #문장 교체, 다만 본래의 값에는 영향이 없음
print(sentence)

index = sentence.index("A") #A의 순서
print(index)
#index =sentence.index("A",index+1)  #다음 A를 찾는 법

print(sentence.find("A")) #A의 순서, 문자가 없으면 -1을 출력

print(sentence.count("A")) #A의 등장 횟수