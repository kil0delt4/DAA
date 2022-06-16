V = 4
INF = 99999

def floydWarshall(graph):
      
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    solution(graph)

def solution(graph):
    for i in range(V):
        for j in range(V):
            if graph[i][j] == INF:
                print("INF", end=" ")
            else:
                print(graph[i][j], end=" ")
        print(" ")
    

G =[[0, 5, INF, INF],
         [50, 0, 15, 5],
         [30, INF, 0, 15],
         [15, INF, 5, 0]]
        
floydWarshall(G)