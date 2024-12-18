# 문제 출처: 백준 119636번
# 문제 제목: 요요 시뮬레이션
# 문제 링크: https://www.acmicpc.net/problem/19636

import math

def diet(day, w0, i0, t, i, a) :
    m1 = i0
    w1 = w0

    for j in range(1, day+1):
        
        # 변화 S 계산
        s1 = m1 + a
        
        # w += i - s 계산
        # 1. 변화 X -> i - (i0 + a)
        w0 += i - (i0 + a)
        # 2. 변화 O -> i - s1
        w1 += i - s1
        
        if abs(i - s1) > t :
            m1 += math.floor((i-s1)/2)
            
        
    return w0, w1, m1
    
def printResult(w, m, mode, i0=None, a0=None) :
    if w <= 0 or m <= 0 :
        print("Danger Diet")
    else :
        result = ""
        if mode == 1 :
            if i0 - (m + a0) > 0 :
                result = "YOYO"
            else :
                result = "NO"
        print(w, m, result)

w, i0, t = map(int, input().split())
day, i, a = map(int, input().split())

w0, w1, m1 = diet(day, w, i0, t, i, a)
printResult(w0, i0, 0)
printResult(w1, m1, 1, i0, 0)