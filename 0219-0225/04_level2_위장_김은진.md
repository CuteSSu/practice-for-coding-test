# level2_위장
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42578   
풀이에 걸린 시간 : 4분  

## 문제 설명
```python
# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장

# 스파이가 가진 의상들이 담긴 2차원 배열 clothes
# 서로 다른 옷의 조합의 수를 return

# 같은 이름을 가진 의상은 존재하지 않습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.
```

## 문제 접근 방법
```python
# 스파이는 하루에 최소 한 개의 의상은 입습니다
# -> 전체 - (스파이가 아무것도 안 입는 경우)
```

## 맞은 코드
```python
def solution(clothes):
    answer = 1

    dic = dict()

    # 의상 종류 별 갯수
    for val, key in clothes:
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
    # print(dic)

    for i in dic.values():
        answer *= i + 1  # (i + 1)인 이유 : 0, 1, ..., i -> (i + 1) 개 
    return answer - 1  # 전체 - (스파이가 아무것도 안 입는 경우) = 전체 - 1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
```
* 시간복잡도 : O(n)
