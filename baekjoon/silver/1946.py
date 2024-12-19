# 문제 출처: 백준 1946번
# 문제 제목: 신입 사원
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

def find_passed_count(n) :
    count = 1
    candidates = []
    for i in range(n) :
        document_score, interview_score = map(int, input().split())
        candidates.append((document_score, interview_score))
        
    candidates.sort(key = lambda x: (x[0]))
    
    threshold = candidates[0][1]
    for i in range(1, n) :
        if threshold > candidates[i][1] :
            count += 1
            threshold = candidates[i][1]
        
            
    return count

t = int(input().rstrip())

while t :
    n = int(input().rstrip())
    print(find_passed_count(n))
    t -= 1