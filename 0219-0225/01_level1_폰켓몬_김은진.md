# level1_폰켓몬
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845 
풀이에 걸린 시간 : 7분  

## 문제 설명
```python
# 홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
# 폰켓몬은 종류에 따라 번호를 붙여 구분
# 같은 종류의 폰켓몬은 같은 번호

# 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택

# N마리 폰켓몬의 종류 번호가 담긴 배열 nums
# N/2마리의 폰켓몬을 선택하는 방법 중,
    # 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return

# nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, "항상 짝수"
```

## 문제 접근 방법
```python
# 폰켓몬 종류가 중복으로 나옴 -> dict 사용

# 일단 dict 사용해서 key별 value를 셈
# key가 N/2보다 작으면 key갯수 return
# 아니면 N/2 return
```

## 맞은 코드
```python
def solution(nums):
    dic = dict()

    # 딕셔너리에 (key, value) 저장
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    if len(dic) <= len(nums) // 2: # key가 N/2보다 작은 경우 key 갯수 return
        return len(dic)
    else: # 아니면 N/2 return
        return len(nums) // 2


print(solution([3,1,2,3]))
```
