#리스트 (순서를 가지는 객체) 

subway=[10, 20, 30]

print(subway)

print(subway.index(10))
print(subway.index(20))
print(subway.index(30))

subway.append(40)
print(subway)

subway.insert(0, -10)
print(subway)

subway.pop()
print(subway)
subway.pop()
print(subway)
subway.pop()
print(subway)

subway.append(40)
subway.append(20)
subway.append(20)
print(subway)
print(subway.count(20))

subway.sort()
print(subway)
subway.reverse()
print(subway)

subway.clear()
print(subway)

#리스트엔 자료형에 상관x, 막 넣을 수 있다.

list1 =['a','b',0]
list2=[1,2,"3"]

list1.extend(list2) #확장
print(list1)