import sys
input = sys.stdin.readline

n=int(input()) 
l=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    l.append(tmp)

def 합치기(graph,방향):
    if 방향==1: #상
        for j in range(n):
            p = 0

            for i in range(1, n):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0

                    if graph[p][j] == 0:
                        graph[p][j] = temp

                    elif graph[p][j] == temp:
                        graph[p][j] *= 2
                        p += 1

                    else:
                        p += 1
                        graph[p][j] = temp
    elif 방향==2: #하
        for j in range(n):
            p = n - 1

            for i in range(n - 2, -1, -1):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0

                    if graph[p][j] == 0:
                        graph[p][j] = temp
                    elif graph[p][j] == temp:
                        graph[p][j] *= 2
                        p -= 1
                    else:
                        p -= 1
                        graph[p][j] = temp
        
    elif 방향==3: #좌
        for i in range(n):
                p = 0

                for j in range(1, n):
                    if graph[i][j]:
                        temp = graph[i][j]
                        graph[i][j] = 0

                        if graph[i][p] == 0:
                            graph[i][p] = temp
                        elif graph[i][p] == temp:
                            graph[i][p] *= 2
                            p += 1
                        else:
                            p += 1
                            graph[i][p] = temp
                
    elif 방향==4: #우
        for i in range(n):
            p = n - 1

            for j in range(n - 2, -1, -1):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0

                    if graph[i][p] == 0:
                        graph[i][p] = temp
                    elif graph[i][p] == temp:
                        graph[i][p] *= 2
                        p -= 1
                    else:
                        p -= 1
                        graph[i][p] = temp
    return graph

def 검사(al,bl):
    for i in range(n):
        for j in range(n):
            if al[i][j]!=bl[i][j]:
                return True
    return False

    
def dfs(c,board):
    global maxx
    global max_branch
    if c==10:
        tmp=0
        for i in board:
            tmp=max(tmp,max(i))
        if maxx<tmp:
            maxx=tmp
            for i in range(10,-1,-1):
                max_branch[i]=tmp
                tmp//=2
        return

    가능성=False
    for x in range(n):
        for y in range(n):
            if board[x][y]>max_branch[c]: 
                가능성=True
                break
    if 가능성==True:
        for i in range(1,5):
            tmp_board=합치기( [item[:] for item in board],i)
            if 검사(board,tmp_board)==True:
                dfs(c+1,tmp_board)
maxx=0
for i in l:
    maxx=max(maxx,max(i))
max_branch=[0]*11
dfs(0,l)
print(maxx)
