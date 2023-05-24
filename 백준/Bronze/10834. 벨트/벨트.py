def main() :
 
    # 입력
    M = int(input())
 
    # 초기화
    resultDir = 0
    resultCnt = 1
    
    # 구현
    for _ in range(M) :
        first, second, dir = map(int, input().split())
        resultDir = resultDir ^ dir
        resultCnt = resultCnt // first * second
 
    # 출력
    print(resultDir, resultCnt)
 
if __name__ == '__main__' :
    main()
