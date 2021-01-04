from collections import OrderedDict

# 일반적인 dict 는 순서를 보장하지 않음
d = {}
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)

# OrderedDict 는 순서 보장
d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)

# 키값을 기준으로 정렬하여 OrderedDict 를 생성
for k, v in OrderedDict(sorted(d.items(), key = lambda t : t[0])).items() :
    print(k, v)

# 밸류값을 기준으로 역순 정렬하여 OrderedDcit 생성
for k, v in OrderedDict(sorted(d.items(), reverse = True, key = lambda t : t[1])).items():
    print(k, v)