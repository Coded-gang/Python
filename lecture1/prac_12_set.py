#집합 set
# 중복 금지, 순서 없음

set1 ={1,2,3,3,3,2}
print(set1)

lecture1={"전자기학","디논설","공업수학"}
lecture2 = set(["전자기학","공업수학","물리전자"])
#리스트로 선언하고 set으로 감싸줄 수 있다.
print(lecture1 & lecture2)
print(lecture1.intersection(lecture2))
#교집합

print(lecture1 | lecture2)
print(lecture1.union(lecture2))
#합집합

print(lecture1 -lecture2) #차집합

lecture1.add("프로그래밍실습")
print(lecture1)

lecture1.remove("전자기학")
print(lecture1)

# set {} key{3:}
#() topple
#[]list