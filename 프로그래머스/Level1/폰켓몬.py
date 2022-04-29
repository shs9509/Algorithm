# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    length = len(nums)
    set_len = len(set(nums))
    if length//2 <= set_len:
        answer = length//2
    else:
        answer = set_len
    return answer