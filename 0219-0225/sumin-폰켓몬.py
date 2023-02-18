# https://school.programmers.co.kr/learn/courses/30/lessons/1845

"""
[문제 이해]
선택해야되는 개수는 nums/2 개고 최대의 갯수를 구하는거다. 
따라서 2가지 케이스를 나눌 수다. 
1. 폰켓몬 종류의 갯수가 구해야되는 갯수보다 클때
    -> [3, 1, 2, 3]은 종류는 3종류, 구해야되는 갯수는 2개이다.
    -> 이럴경우 그냥 구해야되는 갯수를 return 하면 된다. 
    -> 왜냐하면 종류가 구해야되는 갯수보다 많아서 어떤 조합이던 상관없이 2개를 고를 수 있기 때문이다. 
2. 폰켓몬 종류의 갯수가 구해야되는 갯수보다 작을때 
    -> [2, 2, 2, 3, 3, 3]은 종류는 2개, 구해야되는 갯수는 3개이다. 
    -> 이럴경우 종류갯수를 return 하면 된다.
    -> 왜냐하면 어떤 조합이든 종류 수밖에 나오지 않아 종류 갯수가 최대값이기 때문이다. 

[문제 풀이]
파이썬에서 set 함수는 중복을 제거해준다. 따라서 set 함수를 사용하여 nums의 폰켓몬 종류 개수를 구해서 if문을 통해 케이스를 나눠 return 해준다. 
"""

def solution(nums):
    answer = 0
    type_num = len(set(nums))
    get_num = len(nums)/2
    
    if type_num > get_num:
        answer = get_num
    else:
        answer = type_num
        
    return answer