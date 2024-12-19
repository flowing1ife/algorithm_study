# 문제 출처: 백준 9375번
# 문제 제목: 패션왕 신해빈
# 문제 링크: https://www.acmicpc.net/problem/9375

def countClothingCombinations(n) :
    clothing = {}
    result = 1
    for i in range(n) :
        clothing_name, clothing_type = input().split()
        
        if clothing_type in clothing :
            clothing[clothing_type] += 1
        else :
            clothing.update({clothing_type : 1})
            
    for cloth, value in clothing.items() : 
        result *= (value+1)
        
    return result - 1

t = int(input().rstrip())

while t : 
    n = int(input().rstrip())
    print(countClothingCombinations(n))
    t -= 1