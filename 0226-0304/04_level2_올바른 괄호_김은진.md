# level2_올바른 괄호
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12909  
풀이에 걸린 시간 : 5분  

## 문제 설명
```python
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻
# '(' 또는 ')' 로만 이루어진 문자열 s
# 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return
```

## 문제 접근 방법
```python
# stack(스택) 사용 -> stack(스택) 사용 안하고, cnt만 계산해도 되어서 cnt만 계산!
```

## 맞은 코드
```python
def solution(s):
    cnt = 0

    for val in s:
        if val == '(':  # '('일 경우
            cnt += 1 # 카운트 증가
        else:  # ')'일 경우
            if cnt <= 0: # 카운트가 0이거나 음수인 경우 -> (보다 )가 먼저 나왔거나, )의 갯수가 많이 나온 경우
                return False
            cnt -= 1  # 카운트가 양수인 경우 
    if cnt != 0:  # 짝이 안 맞을 경우
        return False
    return True


solution("()()")
```
* 시간복잡도 : O(n)
