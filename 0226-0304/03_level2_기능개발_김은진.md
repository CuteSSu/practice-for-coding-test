# level2_기능개발
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586  
풀이에 걸린 시간 : 30분  

## 문제 설명
```python
# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
    # 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 정수 배열 speeds

# 각 배포마다 몇 개의 기능이 배포되는지를 return

# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정
```

## 문제 접근 방법
```python
# ceil((100 - progresses) / speeds) => 100%에 도달하게 되는 시간
# 앞에서부터 차례대로 계산
```

## 맞은 코드
```python
from math import ceil


def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        progresses[i] = ceil((100 - progresses[i]) / speeds[i]) # 100%에 도달하게 되는 시간
    # print(progresses)

    start = progresses[0] # 배포가 시작되는 값
    temp = 0 # 배포 갯수
    for progress in progresses:
        if start >= progress: # 배포가 가능
            temp += 1
        else: # 배포가 불가능
            answer.append(temp) # answer에 값 넣기
            start = progress # 배포가 시작되는 값 갱신
            temp = 1 # 배포 갯수 갱신
    if temp != 0: # 마지막에 배포를 놓칠 경우를 방지
        answer.append(temp)
    # print(answer)

    return answer


solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
```
* 시간복잡도 : O(n)
* 예전엔 10분 이내로 풀었는데... 나의 코테 실력 퇴화했다ㅠ 노력하자ㅠ
* 시간이 오래 걸린 부분은 answer 값을 만드는 부분이었는데, stack을 사용하면 쉽게 해결 할 수 있었다..
  * 참조 링크 : https://d-tail.tistory.com/70
  * 일단 뽑고, 비교를 하기
    * 더 작거나 같으면 temp += 1
    * 더 크면 answer에 값 넣고, temp = 1 갱신
