# 빈칸을 기준으로 문자열 나누기
items = 'zero one two three'.split()
print(items)

# ',' 를 기준으로 문자열 나누기
example = 'python,jquery,javascript'
print(example.split(','))

# 리스트의 각 값을 a, b, c 변수로 unpacking
a, b, c = example.split(',')
print(a, b, c)