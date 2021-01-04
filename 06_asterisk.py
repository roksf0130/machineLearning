# 함수의 전달인자 수가 가변일 때 '*' 를 이용, tuple 형태로 전달
def asterisk_test(a, *args) :
    print(a, args)
    print(type(args))
asterisk_test(1, 2, 3, 4, 5, 6)

# 함수의 전달인자 수가 가변일 때 '**' 를 이용하면 변수명과 값이 dict 형태로 전달
def asterisk_test(a, **kargs) :
    print(a, kargs)
    print(type(kargs))
asterisk_test(1, b = 2, c = 3, d = 4, e = 5, f = 6)

# 튜플을 아규먼트로 넘길 때는 튜플의 튜플형태가 되기 때문에 인덱스를 명시해야 함
def asterisk_test(a, *args) :
    print(a, args[0])
    print(type(args))
asterisk_test(1, (2, 3, 4, 5, 6))

# 전달받은 함수에서 '*' 를 이용해 unpacking
def asterisk_test(a, args):
    print(a, *args)
    print(type(args))
asterisk_test(1, (2, 3, 4, 5, 6))

# '*' 를 이용한 unpacking
a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)
data = ([1, 2], [3, 4], [5, 6])
print(*data)

for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))

# dict 를 '**' 로 함수 아규먼트 전달
def asterisk_test(a, b, c, d, e = 0) :
    print(a, b, c, d, e)
data = {"d" : 1 , "c" : 2, "b" : 3, "e" : 56}
asterisk_test(10, **data)
