# level2_전화번호 목록
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577   
풀이에 걸린 시간 : 7분  

## 문제 설명
```python
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true
# 같은 전화번호가 중복해서 들어있지 않습니다.
```

## 문제 접근 방법
```python
# 일단 정렬을 해서, 나보다 바로 뒤인 애가 부분 집합인지 체크
# 이렇게 풀어도 되는 이유 : 정렬을 하면 접두사인 애는 나의 바로 뒤에 있을 수 밖에 없기 때문
```

## 맞은 코드
```python
def solution(phone_book):
    phone_book.sort() # 정렬
    # print(phone_book)

    for i in range(len(phone_book) - 1):
        length = len(phone_book[i]) # 접두사 길이
        if phone_book[i] == phone_book[i + 1][:length]: # 접두사 체크 
            return False
    return True


solution(["119", "97674223", "1195524421"])
```
* 시간복잡도 : O(nlogn) -> sort 사용
* defaultDict로 푸는 방법도 알아두면 좋을 거 같다!! 
  * from collections import defaultDict
  * defaultDict의 특이한 점 : type을 지정, 값을 지정하지 않으면 0
  * defaultDict 참조 링크 : https://dongdongfather.tistory.com/69