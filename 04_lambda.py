# 일반적인 함수 선언 및 호출
def f(x, y) :
    return x + y
print(f(1, 4))

# 람다함수 사용하기
f = lambda x, y : x + y
print(f(1, 4))

f = lambda x : x ** 2
print(f(3))

f = lambda x : x / 2
print(f(3))

print((lambda x : x + 1)(5))