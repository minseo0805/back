import math
a, b, v = map(int, input().split()) #a 올림 b 내림 v 막대 
answer = math.ceil((v-b) / (a-b)) #math.ceil올림함수 
print(answer)