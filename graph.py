n,e=map(int,input().split())
adjlist=[ [  ] for i in range(n)]

def Print_path(u,v,visited):
    visited[u]=True
    path.append(u)
    if u==v:
       print(path)

    else:
        for i in adjlist[u]:
            if not visited[i]:
                Print_path(i,v,visited)
    path.pop()
    visited[u]=False

for i in range(e):
    u,v=map(int,input().split())
    adjlist[u].append(v)
    adjlist[v].append(u)
for i in adjlist:
    print('--->',i)
path=[]
visited = [False for i in range(n)]
#dfs(2,3, visited)
#print_path(2,3)
Print_path(2,3,visited)
