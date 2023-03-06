# level2_같은 숫자는 싫어
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12906   
풀이에 걸린 시간 : 3분  

## 문제 설명
```python
# 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져
# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return
```

## 문제 접근 방법
```python
# 스택을 사용해서 가장 끝만 비교
    # 스택에 아무런 값이 없을 경우에만 그냥 값을 넣어줌
```

## 맞은 코드
```python
def solution(arr):
    answer = []  # 스택처럼 사용

    for a in arr:
        if len(answer) == 0:  # 스택에 아무런 값이 없을 경우
            answer.append(a)
        else:
            if answer[-1] == a:  # 스택의 가장 마지막 값과 배열 값이 같을 경우
                continue
            else:  # 스택의 가장 마지막 값과 배열 값이 다를 경우
                answer.append(a)
    # print(answer)

    return answer


solution([1,1,3,3,0,1,1])
```
* 시간복잡도 : O(n)
