if __name__=='__main__':
    N = int(input())
    if N==0: ans = 1
    elif N%2 == 0 : ans=(N//2+1)**2
    else : ans = (N//2+1)*(N//2+2)
    print(ans)