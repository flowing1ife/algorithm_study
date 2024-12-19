# 문제 출처: 백준 14425번
# 문제 제목: 문자열 집합
# 문제 링크: https://www.acmicpc.net/problem/14425

n, m = map(int, input().split())
str_set = set()
result = 0

for i in range(n) :
    str_set.add(input().rstrip())
    
for i in range(m) :
    if input().rstrip() in str_set :
        result += 1
        
print(result)