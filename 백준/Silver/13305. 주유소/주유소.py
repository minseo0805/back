N = int(input())
roads = list(map(int, input().split())) #도로
cities = list(map(int, input().split())) #도시

minVal = cities[0] #첫 도시의 기름값 
sum = 0
for i in range(N-1):
    if minVal > cities[i]: #도시의 기름값이 더 작으면 
        minVal = cities[i] #그값으로minVal을 바꿈
    sum += (minVal * roads[i]) #도로 길이를 곱한 값을 sum에 더함 
    
print(sum)