print("a"+"b")
print("a","b")

#방법 1

print("나는 %d살입니다." %24)
print("나는 %s를 좋아해요" % "너")
print("Apple은 %c로 시작해요" %"a")

print("나는 %s살입니다." %24)  # %s가 만능키

print("%d + %d = %s 입니다."%(1,2,"삼") )

#방법 2
print("나는 {}살입니다." .format(24))
print("{}+{}={}" .format(1,2,"삼"))
print("{2}+{1}={0}" .format(1,2,"삼"))

#방법3
print("{first}+{second}={third}" .format(first=1,third=3,second=2))

#방법 4
age =24
color = "red"
print(f"난 {age}살이고 {color}를 좋아해요")