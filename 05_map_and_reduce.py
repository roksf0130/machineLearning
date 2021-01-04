# map 함수를 이용하여 리스트 각각의 엘리먼트에 람다함수 적용
ex = [1, 2, 3, 4, 5]
f = lambda x : x ** 2
print(list(map(f, ex)))

# 여러개의 리스트를 전달하는 것도 가능
ex = [1, 2, 3, 4, 5]
f = lambda x, y : x + y
print(list(map(f, ex, ex)))

# map 함수에 람다 사용하기 - else 문은 필수
print(list(map(lambda x : x ** 2 if x % 2 == 0 else x, ex)))

# 형변환을 위해 list를 꼭 붙여줘야함
ex = [1, 2, 3, 4, 5]
print(list(map(lambda x : x + x, ex)))
print((map(lambda x : x + x, ex)))

# 형번환을 위한 list 대신 for loop 사용 가능
f = lambda x : x ** 2
print(map(f, ex))
for i in map(f, ex):
    print(i)

# next 사용
result = map(f, ex)
print(result)
print(next(result))

import sys
print(sys.getsizeof(ex))
print(sys.getsizeof((map(lambda x : x + x, ex))))
print(sys.getsizeof(list(map(lambda x : x + x, ex))))

# reduce
from functools import reduce
print(reduce(lambda x, y : x + y, [1, 2, 3, 4, 5]))

# reduce 함수를 이용한 팩토리얼 구하기
def factorial(n):
    return reduce(lambda x, y : x * y, range(1, n + 1))
print(factorial(5))