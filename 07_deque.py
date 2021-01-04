from collections import deque

# deque 리스트 생성
deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

# 리스트의 왼쪽에 엘리먼트 추가
deque_list.appendleft(10)
print(deque_list)

# 리스트의 가장 오른쪽 엘리먼트를 제거하고 왼쪽에 추가 (2회)
deque_list.rotate(2)
print(deque_list)

# 리스트의 순서를 역순으로 만듬
print(deque(reversed(deque_list)))

# 리스트 확장 - 새로운 엘리먼트를 오른쪽에 추가
deque_list.extend([5, 6, 7])
print(deque_list)

# 리스트 확장 - 새로운 엘리먼트를 왼쪽에 추가
deque_list.extendleft([5, 6, 7])
print(deque_list)