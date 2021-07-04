def solution(n, times):
    answer = 0
    left=min(times) * n // len(times)
    right=max(times) * n // len(times)
    
    fn=0 # finished number
    for t in times:
        fn+=left//t
    if fn==n:
        return left
    else:
        while left<right:
            fn=0
            # 며칠 걸리는지 체크
            for t in times:
                fn+=(left+right)//2 // t
            if fn>=n:
                right=(left+right)//2
            else:
                left=(left+right)//2 + 1
        return left
