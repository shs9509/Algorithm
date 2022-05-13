# https://programmers.co.kr/learn/courses/18/lessons/1881
def stic(li): #[14, 6, 5, 11, 3, 9, 2]
    tmp = li[0:2] + [ 0 for _ in range(len(li)-2)]
    for i in range(len(li)-2):
        if i == len(li)-3:
            tmp[i+2] = max(tmp[i+2],tmp[i]+li[i+2])
        else:
            tmp[i+2] = max(tmp[i+2],tmp[i]+li[i+2])
            tmp[i+3] = max(tmp[i+3],tmp[i]+li[i+3])
    return(max(tmp))
    
def solution(sticker):
    answer = 0
    if len(sticker)<3:
        return max(sticker)
    fore_tmp = sticker[1:]
    back_tmp = sticker[:-1]
    return max(stic(fore_tmp),stic(back_tmp))