# level1_완주하지 못한 선수
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3  
풀이에 걸린 시간 : 9분  

## 문제 설명
```python
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant
# 완주한 선수들의 이름이 담긴 배열 completion

# 완주하지 못한 선수의 이름을 return

# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
```

## 문제 접근 방법
```python
# parti가 1개가 더 긺
# parti로 비교해서
    # 1) key 값이 없거나
    # 2) val 값이 다른 경우
# 해당 key값을 return 해주면 됨
```

## 맞은 코드
```python
def solution(participant, completion):
    dic1 = dict()  # participant dict
    dic2 = dict()  # completion dict

    # participant dict
    for parti in participant:
        if parti not in dic1:
            dic1[parti] = 1
        else:
            dic1[parti] += 1
    # print(dic1)

    # completion dict
    for compl in completion:
        if compl not in dic2:
            dic2[compl] = 1
        else:
            dic2[compl] += 1
    # print(dic2)

    for key, val in dic1.items():
        if key not in dic2:  # 1) key 값이 없는 경우
            return key
        elif val != dic2.get(key):  # 2) val 값이 다른 경우
            return key


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
```

## 다른 풀이 (Counter 사용)
<img src="https://user-images.githubusercontent.com/72064966/221578026-4c12e662-9338-467a-96eb-21a215ede837.png">

* Counter를 사용하면 dict의 긴 코드를 짧게 줄일 수 있음!!
* from collections import Counter -> 바로 Conuter(x) 이런식으로 작성 가능
* 참고 링크 : https://velog.io/@h986680/TIL.10-%EC%BD%94%ED%85%8C%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98