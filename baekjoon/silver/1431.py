# 문제 출처: 백준 1431번
# 문제 제목: 시리얼 번호
# 문제 링크: https://www.acmicpc.net/problem/1431

def sumNum(serial) :
    return sum(int(ch) for ch in serial if ch.isdigit())
    
def key_function(serial) :
    return (len(serial), sumNum(serial), serial)

n = int(input().rstrip())
guitar = []
for i in range(n) :
    guitar.append(input().rstrip())
    
guitar.sort(key=key_function)

for serial in guitar : 
    print(serial)