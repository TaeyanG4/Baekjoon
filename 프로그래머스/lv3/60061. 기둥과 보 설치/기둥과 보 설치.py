def buildable(x, y, a, res):
    
    # 기둥
    if a == 0:
        # 바닥인 경우
        if y == 0: 
            return True
        
        # 기둥이 있는 경우
        if (x, y - 1, 0) in res:
            return True
        
        # 바닥에 보가 있는 경우
        if (x - 1, y, 1) in res: 
            return True
        
        if (x, y, 1) in res: 
            return True
    # 보
    else:
        # 양끝에 보가 있는경우
        if (x - 1, y, 1) in res and (x + 1, y, 1) in res: 
            return True
        
        # 한쪽 끝에 기둥이 있는경우
        if (x + 1, y - 1, 0) in res or (x, y - 1, 0) in res: 
            return True
    
    return False

def solution(n, build_frame):
    res = []
    
    for x, y, a, b in build_frame:
        
        # bulid
        if b:
            if buildable(x, y, a, res):
                res.append((x, y, a))
        
        # remove
        else:
            res.remove((x, y, a))
            for nx, ny, na in res:
                if not buildable(nx, ny, na, res):
                    res.append((x, y, a))
                    break
    
    res.sort()
    return res