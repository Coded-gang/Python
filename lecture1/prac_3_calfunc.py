print(abs(-5))  # 5
print(pow(4,2)) # 4^2
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 4
print(ceil(3.14)) # 4
print(sqrt(16)) # 4

from random import *
print(random()) # 0.0~1.0 random
print(random()*10) # 0.0~10.0
print(int(random()*10)) #자료형 변환
print(int(random()*10)+1)
print(randrange(1,46)) # 1~45까지 랜덤
print(randint(1,46)) # 1~46